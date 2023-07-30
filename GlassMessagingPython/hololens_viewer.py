# coding=utf-8

# This code is copied from [HeadsUp-PilotAnalyzer](https://github.com/NUS-HCILab/HeadsUp-PilotAnalyzer/blob/main/stream_player.py)

import hololens_config
import cv2

IP = hololens_config.get_ip()
USERNAME = hololens_config.get_username()
PASSWORD = hololens_config.get_password()
SETTINGS = "holo=true&pv=true&mic=false&loopback=false"

import time
from pynput import keyboard
import traceback

KEY_STOP = keyboard.KeyCode.from_char('q')

flag_is_running = False


def run_with_opencv():
    # Replace the video capture attributes based on the need
    cap = cv2.VideoCapture(f"https://{USERNAME}:{PASSWORD}@{IP}/api/holographic/stream/live_med.mp4?{SETTINGS}")
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    # cap = cv2.VideoCapture(0)
    # size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)/2), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)/2))

    cv2.namedWindow("FPV")
    x, y = 0, 0
    # Known Issue: macOS doesn't support move window to negative position
    cv2.moveWindow("FPV", x, y)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame.")
            break

        frame = cv2.resize(frame, size)

        cv2.imshow("FPV", frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

        if not flag_is_running:
            break


def on_press(key):
    global flag_is_running
    if key == KEY_STOP:
        flag_is_running = False
        return False  # stop listener


# run the program
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

flag_is_running = True

while flag_is_running:
    try:
        run_with_opencv()
    except Exception:
        traceback.print_exc(file=sys.stdout)

    time.sleep(0.5)
