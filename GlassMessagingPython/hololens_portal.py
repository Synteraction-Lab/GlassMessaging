# coding=utf-8

import utilities
import hololens_config

# Note: Need to disable SSL connection (System->Preference)

CREDENTIALS = {
    'username': hololens_config.get_username(),
    'password': hololens_config.get_password()
}

# Ref: 
#	- https://docs.microsoft.com/en-us/windows/mixed-reality/develop/advanced-concepts/device-portal-api-reference
#	- https://docs.microsoft.com/en-us/windows/uwp/debug-test-perf/device-portal-api-core
API_BASE = f'http://{hololens_config.get_ip()}'
API_START_RECORDING = f'{API_BASE}/api/holographic/mrc/video/control/start?holo=true&pv=true&mic=true&loopback=true&RenderFromCamera=true'  # POST 
API_STOP_RECORDING = f'{API_BASE}/api/holographic/mrc/video/control/stop'  # POST
API_GET_RECORDINGS = f'{API_BASE}/api/holographic/mrc/files'  # GET
API_GET_RECORDING_STATUS = f'{API_BASE}/api/holographic/mrc/status'  # GET
API_TAKE_PHOTO = f'{API_BASE}/api/holographic/mrc/photo?holo=true&pv=true'  # POST


# return True if success else False
def start_recording():
    return utilities.send_post_request(API_START_RECORDING, "", CREDENTIALS)


# return True if success else False
def stop_recording():
    return utilities.send_post_request(API_STOP_RECORDING, "", CREDENTIALS)


def take_photo():
    return utilities.send_post_request(API_TAKE_PHOTO, "", CREDENTIALS)


# return list of files ([{'CreationTime': xx, 'FileName': 'xx.mp4', 'FileSize': xx}])
def get_saved_recordings():
    res = utilities.send_get_request(API_GET_RECORDINGS, CREDENTIALS)
    if res is None or not res:
        return []

    return res['MrcRecordings']


# return True if recording
def get_recording_status():
    res = utilities.send_get_request(API_GET_RECORDING_STATUS, CREDENTIALS)
    if res is None:
        return False

    return res['IsRecording']

# print(get_saved_recordings())
# start_recording()
# utilities.sleep_seconds(3)
# print(get_recording_status())
# utilities.sleep_seconds(3)
# stop_recording()
# utilities.sleep_seconds(1)
# print(get_recording_status())
# take_photo()
# print(get_saved_recordings())
