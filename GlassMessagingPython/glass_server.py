# coding=utf-8

# socket server to communicate with smart glass app

import json
import socket_server
import time

TYPE_SEPARATOR_CHAR = '|'
DATA_TYPE_DUMMY = 'D'
DATA_TYPE_USER_CONVERSATION = 'U'
DATA_TYPE_CONVERSATION = 'C'
DATA_TYPE_MESSAGE = 'M'
DATA_TYPE_INSTRUCTION_MESSAGE = 'I'

DUMMY_DATA = DATA_TYPE_DUMMY + TYPE_SEPARATOR_CHAR


def start_chat_server():
    socket_server.start_server_threaded()


def stop_chat_server():
    socket_server.stop_server_threaded()


def is_connected():
    return socket_server.is_client_connected()


def send_user_conversation(user_conversation):
    tx_data = json.dumps(user_conversation)
    socket_server.send_data(f'{DATA_TYPE_USER_CONVERSATION}{TYPE_SEPARATOR_CHAR}{tx_data}')


def send_conversation(conversation):
    tx_data = json.dumps(conversation)
    socket_server.send_data(f'{DATA_TYPE_CONVERSATION}{TYPE_SEPARATOR_CHAR}{tx_data}')


def reset_conversation(conversation):
    pass

def send_message(message):
    tx_data = json.dumps(message)
    socket_server.send_data(f'{DATA_TYPE_MESSAGE}{TYPE_SEPARATOR_CHAR}{tx_data}')

def send_instruction_message(message):
    tx_data = json.dumps(message)
    socket_server.send_data(f'{DATA_TYPE_INSTRUCTION_MESSAGE}{TYPE_SEPARATOR_CHAR}{tx_data}')

# return <TYPE, JSON_OBJECT> if available, else send <None, None>
def get_chat_data():
    rx_data = socket_server.receive_data()
    if rx_data is None:
        return None, None
    # <TYPE><TYPE_SEPARATOR><JSON_STRING>
    type_data = rx_data.split(TYPE_SEPARATOR_CHAR)
    return type_data[0], _decode_data(type_data[0], type_data[1])


def _decode_data(type, json_string):
    if type == DATA_TYPE_DUMMY:
        return json_string
    if type == DATA_TYPE_USER_CONVERSATION or type == DATA_TYPE_CONVERSATION or type == DATA_TYPE_MESSAGE:
        object = json.loads(json_string)
        object['server_time'] = round(time.time() * 1000)
        return object

    print(f'Unknown data type: {type}-{json_string}')
    return json_string
