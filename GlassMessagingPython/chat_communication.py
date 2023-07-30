# coding=utf-8

import sys
import time
import traceback
from pynput import keyboard

import chat_data
import glass_server
import log_utility
import participant_config
import process_data
import telegram_server
import utilities

KEY_STOP1 = keyboard.KeyCode.from_char('`')
KEY_STOP2 = keyboard.Key.esc
KEY_ANNOTATE1 = keyboard.Key.right
ANNOTATE1_MESSAGE = 'a1'

DEBOUNCE_SECONDS = 0.4  # 400 ms

last_key = None
last_key_press_time = 0


def keep_key_info(key, key_time):
    global last_key, last_key_press_time
    last_key = key
    last_key_press_time = key_time


def is_key_already_pressed(key, key_time):
    if key == last_key and key_time - last_key_press_time < DEBOUNCE_SECONDS:
        return True
    return False


def on_press(key):
    global flag_is_running
    current_time = time.time()

    # ref: https://buildmedia.readthedocs.org/media/pdf/pynput/latest/pynput.pdf

    if key == KEY_STOP1 or key == KEY_STOP2:
        # cleaning up
        flag_is_running = False
        return False  # stop listener

    # debounce the keys
    if is_key_already_pressed(key, current_time):
        print('You have already pressed: ', key)
        return True

    if key == KEY_ANNOTATE1:
        keep_key_info(key, current_time)
        log_key_annotation(ANNOTATE1_MESSAGE)
        print(f'{ANNOTATE1_MESSAGE} added')


keyboard_listener = None


def start_keyboard_listening():
    global keyboard_listener
    keyboard_listener = keyboard.Listener(on_press=on_press)
    keyboard_listener.start()


def stop_keyboard_listening():
    global keyboard_listener
    keyboard_listener.stop()


def log_key_annotation(annotation):
    # FIXME: use _participant and _session should be removed
    print('')
    log_utility.log_message_info(_participant, _session, annotation, None)


def wait_before_sending_message(message_gap, last_message_sent_millis):
    global flag_is_running

    delay_seconds = message_gap

    if last_message_sent_millis <= 0:
        # FIXME (remove this): set low delay at start
        delay_seconds = delay_seconds / 2
        delay_start_time = utilities.get_current_millis()  # initial delay to send first message
    else:
        delay_start_time = last_message_sent_millis

    while flag_is_running and (
            utilities.get_current_millis() - delay_start_time < delay_seconds * 1000):
        pass


def send_message_or_instruction(chat_server, message, texting_task):
    if texting_task == participant_config.TEXTING_TASK_MULTI:
        chat_server.send_instruction_message(message)
    else:
        chat_server.send_message(message)


def clear_instruction(chat_server, texting_task):
    if texting_task == participant_config.TEXTING_TASK_MULTI:
        message = chat_data.get_empty_message()
        chat_server.send_instruction_message(message)


flag_is_running = False


def start_chat(participant, session, record):
    global flag_is_running

    if flag_is_running:
        print('Another instance is running')
        return

    flag_is_running = True

    is_training = participant_config.is_training(participant, session)
    platform = participant_config.get_platform(participant, session)
    primary_task = participant_config.get_primary_task(participant, session)
    texting_task = participant_config.get_texting_task(participant, session)
    tot_messages_count = participant_config.get_message_count(participant, session)
    message_gap_seconds = participant_config.get_message_gap(participant, session)
    message_length = participant_config.get_message_length(participant, session)

    log_utility.log_participant_info(participant, session, platform, primary_task, texting_task,
                                     message_length)

    if platform == participant_config.PLATFORM_PHONE:
        chat_server = telegram_server
    elif platform == participant_config.PLATFORM_GLASS:
        chat_server = glass_server
    elif platform == participant_config.PLATFORM_NONE:
        chat_server = None
        log_utility.log_message_info(participant, session, 'start', None)
    else:
        print('Error: Unexpected platform')
        return

    # start keyboard listening
    start_keyboard_listening()
    # start chat server
    if chat_server is not None:
        chat_server.start_chat_server()

    sent_message_count = 0
    received_message_count = 0
    chat_server_connected = False
    sent_message_time = 0

    while chat_server is not None and flag_is_running:
        if chat_server_connected != chat_server.is_connected():
            chat_server_connected = chat_server.is_connected()

            if chat_server_connected:
                # send initial data
                send_initial_chat_data(platform, chat_server)
                log_utility.log_message_info(participant, session, 'server_start', None)

        chat_type_data = chat_server.get_chat_data()
        if chat_type_data[0] == 'M':
            receiving_message = chat_type_data[1]

            if received_message_count == 0:
                log_utility.log_message_info(participant, session, 'start', None)

            received_message_count += 1
            print(f'Received message: {received_message_count}, {receiving_message}')
            log_utility.log_message_info(participant, session, 'client', receiving_message)

            clear_instruction(chat_server, texting_task)

            # FIXME: send stop message when sent_message_count >= threshold
            if received_message_count > tot_messages_count:  # start message is excluded
                send_message_or_instruction(chat_server, chat_data.get_empty_message(),
                                            texting_task)
                log_utility.log_message_info(participant, session, 'server', None)
                # stop sending the messages
                break

            wait_before_sending_message(message_gap_seconds, sent_message_time)

            sending_message = chat_data.get_random_message(platform, texting_task, participant,
                                                           message_length,
                                                           is_training)
            send_message_or_instruction(chat_server, sending_message, texting_task)

            sent_message_count += 1
            sent_message_time = utilities.get_current_millis()
            log_utility.log_message_info(participant, session, 'server', sending_message)

        elif chat_type_data[0] is not None:
            print(f'Error: Unexpected data {chat_type_data[0]}-{chat_type_data[1]}')

    print(f'\n---\nTotal messages sent: {sent_message_count}\n---')

    while flag_is_running:
        # wait until experimenter stop the session
        pass

    print(f'Stopping...')
    log_utility.log_message_info(participant, session, 'stop', None)

    # stop chat server
    if chat_server is not None:
        log_utility.log_message_info(participant, session, 'server_stop', None)
        chat_server.stop_chat_server()
    # stop keyboard listening
    stop_keyboard_listening()

    process_participant_data(participant, session)


def send_initial_chat_data(platform, chat_server):
    chat_server.send_user_conversation(chat_data.get_init_user_conversation())
    for temp_cov in chat_data.get_init_conversations(platform):
        chat_server.send_conversation(temp_cov)

    if platform == participant_config.PLATFORM_GLASS:
        for temp_msg in chat_data.get_init_messages(platform):
            chat_server.send_message(temp_msg)


def process_participant_data(participant, session):
    try:
        process_data.process_participant_session(participant, session)
    except Exception:
        print("Error in data processing")
        traceback.print_exc(file=sys.stdout)


def is_valid_session(participant, session):
    if session is None or session == "":
        return False

    return -4 <= utilities.get_int(session) <= 4


_participant = input("Participant (e.g., p1)?")
_session = input("Session (e.g., 1-4)?")

_record = False

try:
    if is_valid_session(_participant, _session):
        start_chat(_participant, _session, _record)
    else:
        print("Invalid session")
except Exception:
    traceback.print_exc(file=sys.stdout)
