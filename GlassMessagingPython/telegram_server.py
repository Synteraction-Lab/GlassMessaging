# coding=utf-8

# References: https://github.com/python-telegram-bot/python-telegram-bot
#   - https://github.com/python-telegram-bot/python-telegram-bot/wiki/Introduction-to-the-API
#   - https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot

# Instructions:
#   - make the bot an admin to enable communication

# Note: This one uses a Telegram bot, so the communication has to be started from an actual user to initiate the texting

import logging
import asyncio
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

import json
import sys
import threading
import time
from queue import Queue
import traceback

import utilities

TELEGRAM_BOT_TOKEN_FILE = 'telegram_token.json'

TIMEOUT_SECONDS_WAITING_FOR_DATA = 90

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def get_telegram_token():
    print('Reading Telegram token')
    with open(TELEGRAM_BOT_TOKEN_FILE, 'r') as f:
        data = json.load(f)
    return data['token']


_phone_ip = None


def get_phone_ip():
    global _phone_ip
    if _phone_ip is None:
        with open(TELEGRAM_BOT_TOKEN_FILE, 'r') as f:
            data = json.load(f)
            _phone_ip = data['ip']

    return _phone_ip


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global tx_queue, rx_queue

    #     print(f'{str(update)}')
    #     await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text) # echo

    # see: https://docs.python-telegram-bot.org/en/v20.0a2/telegram.update.html#telegram.Update
    #       - https://docs.python-telegram-bot.org/en/v20.0a2/telegram.message.html#telegram.Message

    message_obj = update.message
    message_datetime = message_obj.date
    # print(message_datetime)
    rx_data = {
        'conversation_id': message_obj.chat.id,
        'sender': message_obj.chat.title,
        'time': int(message_datetime.now().timestamp() * 1e3),
        'content': message_obj.text,
        'read': False,
        'server_time': round(time.time() * 1000),
    }
    rx_queue.put_nowait(rx_data)
    print(f'Received data: {rx_data}')

    # wait for data if more available
    try:
        tx_data = tx_queue.get(block=True, timeout=TIMEOUT_SECONDS_WAITING_FOR_DATA)
        if tx_data['chat_id'] is not None:
            await context.bot.send_message(chat_id=tx_data['chat_id'], text=tx_data['text'])
            print(f'Sent data: {tx_data}')
        else:
            print('Discarding data with empty chat_id')

        del tx_data
    except Exception:
        traceback.print_exc(file=sys.stdout)

    # # wait a few milliseconds if the queue is empty (TODO: remove this)
    # current_millis = utilities.get_current_millis()
    # while tx_queue.empty() and utilities.get_current_millis() - current_millis < 50:
    #     pass

    # send more data if available
    while not tx_queue.empty():
        tx_data = tx_queue.get_nowait()
        if tx_data['chat_id'] is not None:
            await context.bot.send_message(chat_id=tx_data['chat_id'], text=tx_data['text'])
            print(f'Sent data: {tx_data}')
        else:
            print('Discarding data with empty chat_id')

        del tx_data


tx_queue = Queue()
rx_queue = Queue()

telegram_bot = None


def start_telegram_bot():
    global telegram_bot

    asyncio.set_event_loop(asyncio.new_event_loop())

    # see https://docs.python-telegram-bot.org/en/v20.0a2/telegram.ext.application.html
    telegram_bot = ApplicationBuilder().token(get_telegram_token()).build()

    message_handler = MessageHandler(filters.TEXT, message)
    telegram_bot.add_handler(message_handler)

    telegram_bot.run_polling()


async def stop_telegram_bot():
    global telegram_bot

    await telegram_bot.shutdown()


telegram_thread = None


def start_telegram_threaded():
    global telegram_thread

    telegram_thread = threading.Thread(target=start_telegram_bot, daemon=True)
    telegram_thread.start()


def stop_telegram_threaded():
    global telegram_thread
    #     stop_telegram_bot()

    telegram_thread.join(timeout=3)


def _send_data(chat_id, text):
    global tx_queue

    print(f'tx_size: {tx_queue.qsize()}')

    tx_data = {'chat_id': chat_id, 'text': text}
    tx_queue.put_nowait(tx_data)


def _receive_data():
    global rx_queue

    if rx_queue.empty():
        return None

    print(f'rx_size: {rx_queue.qsize()}')

    return rx_queue.get_nowait()


### phone app interface

def _send_display_data(message):
    display_data = {
        "heading": message['content'],
        "subheading": "",
        "content": "",
        "audio": "none",  # none|beep|sound
        "config": "none",  # none|vibrate
    }
    if not utilities.is_empty(message['content']):
        display_data["audio"] = "beep"
        display_data["config"] = "vibrate"

    display_url = 'http://' + get_phone_ip() + ':8080/displays/10/'
    max_attempts = 2

    attempt = 0
    success = False
    while not success and attempt < max_attempts:
        success = utilities.send_post_request(display_url, display_data)
        attempt += 1

        if not success and attempt < max_attempts:
            utilities.sleep_seconds(0.5)

    return success


### common interface

def start_chat_server():
    start_telegram_threaded()


def stop_chat_server():
    stop_telegram_threaded()


def is_connected():
    return True


def send_user_conversation(user_conversation):
    # do nothing
    pass


def send_conversation(conversation):
    # do nothing
    pass


#     _send_data(conversation['id'], f'-----------------')
#     messages = conversation['messages']
#     for message in messages:
#         send_message(message)


def reset_conversation(conversation):
    _send_data(conversation['id'], f'Hi, how are you?')
    _send_data(conversation['id'], f'Nice to meet you!')


def send_message(message):
    _send_data(message['conversation_id'], message['content'])


def send_instruction_message(message):
    _send_data(message['conversation_id'], message['content'])
    _send_display_data(message)


# return <TYPE, JSON_OBJECT> if available, else send <None, None>
def get_chat_data():
    rx_data = _receive_data()
    if rx_data is None:
        return None, None

    return 'M', rx_data

# start_chat_server()
# send_message({'conversation_id': -708515257, 'content': '_________Hi_'})
# time.sleep(120)
# stop_chat_server()
# time.sleep(5)


# _send_display_data({'content': "hello"})
