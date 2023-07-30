# coding=utf-8

import telegram_server
import chat_data
import time

telegram_server.start_chat_server()

for temp_cov in reversed(chat_data.get_init_conversations("phone")):
    telegram_server.reset_conversation(temp_cov)
time.sleep(25)

telegram_server.stop_chat_server()
