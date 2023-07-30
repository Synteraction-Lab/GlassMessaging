# coding=utf-8

import utilities

import chat_data

# participant log

PARTICIPANT_KEY_ID = "id"
PARTICIPANT_KEY_SESSION = "session"
PARTICIPANT_KEY_PLATFORM = "platform"
PARTICIPANT_KEY_PRIMARY_TASK = "primary_task"
PARTICIPANT_KEY_TEXTING_TASK = "texting_task"
PARTICIPANT_KEY_TEXTING_LENGTH = "texting_length"
PARTICIPANT_KEY_TIME = "time"


def _get_participant_log_file(participant):
    return f'data/{utilities.get_date()}/{participant}/{participant}_config.csv'


def log_participant_info(participant, session, platform, primary_task, texting_task,
                         texting_length):
    file_name = _get_participant_log_file(participant)
    print(
        f'Participant info: {participant}, session: {session}, platform: {platform}, task: {primary_task}, texting: {texting_task}, length: {texting_length}')

    if not utilities.is_file_exists(file_name):
        utilities.append_data(file_name,
                              f'{PARTICIPANT_KEY_ID},{PARTICIPANT_KEY_SESSION},{PARTICIPANT_KEY_PLATFORM},{PARTICIPANT_KEY_PRIMARY_TASK},{PARTICIPANT_KEY_TEXTING_TASK},{PARTICIPANT_KEY_TEXTING_LENGTH},{PARTICIPANT_KEY_TIME}\n')

    utilities.append_data(file_name,
                          f'{participant},{session},{platform},{primary_task},{texting_task},{texting_length},{utilities.get_current_millis()}\n')


# message_object log
MESSAGE_KEY_TYPE = "type"
MESSAGE_KEY_SERVER_TIME = "server_time"
MESSAGE_KEY_ID = "message_id"
MESSAGE_KEY_SENDER = "sender"
MESSAGE_KEY_CONTENT = "content"
MESSAGE_KEY_TIME = "time"
MESSAGE_KEY_DATA = "data"
MESSAGE_KEY_CONVERSATION_ID = "conversation_id"


def _get_message_log_file(participant, session):
    return f'data/{utilities.get_date()}/{participant}/{participant}_{session}_message_info.csv'


def _get_string_value(object, key):
    val = object.get(key)
    if val is None:
        return ''
    return val


def log_message_info(participant, session, type, message_object):
    file_name = _get_message_log_file(participant, session)

    if not utilities.is_file_exists(file_name):
        utilities.append_data(file_name,
                              f'{MESSAGE_KEY_TYPE},{MESSAGE_KEY_SERVER_TIME},{MESSAGE_KEY_ID},{MESSAGE_KEY_SENDER},{MESSAGE_KEY_CONTENT},{MESSAGE_KEY_TIME},{MESSAGE_KEY_DATA}\n')

    if message_object is None:
        utilities.append_data(file_name,
                              f'{type},{utilities.get_current_millis()},,,,,\n')
    else:
        message_info = '"' + f'{message_object}'.replace('"', '""') + '"'
        message_content = '"' + f'{message_object[MESSAGE_KEY_CONTENT]}'.replace('"', '""') + '"'
        sender_name = chat_data.get_conversation_name_by_platform_id(
            message_object[MESSAGE_KEY_CONVERSATION_ID])  # message_object[MESSAGE_KEY_SENDER]
        utilities.append_data(file_name,
                              f'{type},{_get_string_value(message_object, MESSAGE_KEY_SERVER_TIME)},{_get_string_value(message_object, MESSAGE_KEY_ID)},{sender_name},{message_content},{message_object[MESSAGE_KEY_TIME]:f},{message_info}\n')


# task log
TASK_KEY_ID = "id"
TASK_KEY_TEXT = "text"
TASK_KEY_SUBSTITUTES = "substitutes"
TASK_KEY_DURATION = "duration"


def _get_passage_log_file(participant, session):
    return f'data/{utilities.get_date()}/{participant}/{participant}_{session}_passage_info.csv'


def log_passage_info(participant, session, passage):
    file_name = _get_passage_log_file(participant, session)

    if not utilities.is_file_exists(file_name):
        utilities.append_data(file_name,
                              f'{TASK_KEY_ID},{TASK_KEY_TEXT},{TASK_KEY_SUBSTITUTES},{TASK_KEY_DURATION}\n')

    passage_content = passage[TASK_KEY_TEXT].replace('"', '""')

    utilities.append_data(file_name,
                          f'{passage[TASK_KEY_ID]},"{passage_content}","{passage[TASK_KEY_SUBSTITUTES]}",{passage[TASK_KEY_DURATION]}\n')
