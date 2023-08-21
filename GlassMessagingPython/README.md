# GlassMessagingPython
The socket server to communicator with HoloLens2 in the Unity App


## Installation
- Make sure python3 is installed (tested on Win11)
- Install the library dependencies (Hint: You can install all in one command using `pip install pynput pandas python-Levenshtein opencv-python python-telegram-bot --pre`)
  - Install [pynput](https://pypi.org/project/pynput/)
  - Install [python-telegram-bot --pre](https://github.com/python-telegram-bot/python-telegram-bot)
  - Install [pandas](https://pypi.org/project/pandas/)
  - Install [python-Levenshtein](https://pypi.org/project/python-Levenshtein/)
  - Install [opencv-python](https://pypi.org/project/opencv-python/)
- Create a file `telegram_token.json` with Telegram bot token (Note: json format must be correct) if you want to test with Telegram also (if only HoloLens2 is needed, this is optional)
  - ```json
    {
    "token": "XXXXX",
    "ip": "IP_ADDRESS_OF_PHONE_APP"
    }
    ```
- Run `chat_communication.py` (`python chat_communication.py`)
- Select the participant id (e.g.,  p1) and session id (e.g., 1) according to study settings (e.g., [participant_config.py](participant_config.py))


### HoloLens app
- Install the corresponding mixed reality app in [GlassMessagingUnity](../GlassMessagingUnity)
- Disable SSL for recording videos (Device Portal -> System -> Preference -> SSL connection)


### Phone apps
- Install Telegram and create the contact list via Telegram bot (create the Group with the contact name and Telegram bot, give the bot admin rights, and remove the real person)
- Update the Telegram Group ID in `chat_data.py` (line 317, `PLATFORM_PHONE_CONVERSATION_IDS`)
- Start the Telegram
- Start the Android app in [NIPGlass](https://github.com/NUS-HCILab/NIPGlass/tree/poc/communicator_pilot_1.3)
- Keyboard config [see](phone_keyboard_config.mp4)

## Run the application (sever)
- Connect the computer (server that runs this code) and HoloLens to the same PRIVATE network (e.g., your phone's hotspot)
- Identify the IP address of the computer/server
- Configure the HoloLens to support the IP address of the computer/server (see [GlassMessagingUnity](../GlassMessagingUnity))

### Ring mouse
- Model: Sanwa Supply 400-MA077 (Sanwa Ring Mouse 2)
- See ![key mapping](ring_mouse_config.png)



