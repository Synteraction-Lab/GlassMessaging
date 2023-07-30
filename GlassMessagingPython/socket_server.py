# coding=utf-8

# References

# - python server
#   - https://www.geeksforgeeks.org/socket-programming-python/#:~:text=Socket%20programming%20is%20a%20way,reaches%20out%20to%20the%20server.
#   - https://realpython.com/python-sockets/

# - sources
#   - https://medium.datadriveninvestor.com/connecting-the-microsoft-hololens-and-raspberry-pi3b-58665032964c


import sys
import threading
import socket
import time
from queue import Queue
import traceback

DATA_END_CHAR = '\r\n'
IGNORE_DATA = 'D|'

PORT = 8080
HOST = ""  # socket.gethostname(), from any computer

SERVER_STATUS_STARTED = "STARTED"
SERVER_STATUS_STOPPED = "STOPPED"
SERVER_STATUS_CONNECTED = "CONNECTED"
SERVER_STATUS_DISCONNECTED = "DISCONNECTED"

server_status = SERVER_STATUS_STOPPED

tx_queue = Queue()
rx_queue = Queue()


def start_server():
    global tx_queue, rx_queue, server_status

    if server_status != SERVER_STATUS_STOPPED :
        print('A server instance is running')
        return

    server_status = SERVER_STATUS_STARTED

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        print(f'server starting:: host: {HOST}, port: {PORT}')
        server_socket.bind((HOST, PORT))

        # put socket to listing mode
        server_socket.listen(5)

        print('server listening')
        while True:
            (client_socket, address) = server_socket.accept()
            with client_socket:
                print(f'Connection from : {address}')
                server_status = SERVER_STATUS_CONNECTED

                while True:
                    try:
                        # decode Bytes
                        data = client_socket.recv(1024)

                        if not data or server_status == SERVER_STATUS_STOPPED:
                            break

                        # remove <MESSAGE_END_CHAR>
                        rx_data = str(data.decode('utf-8')).replace(DATA_END_CHAR, '')

                        # ignore <IGNORE_MESSAGE>
                        if not rx_data.startswith(IGNORE_DATA):
                            rx_queue.put_nowait(rx_data)
                            print(f'Received data: {str(data)}, {rx_data}')

                        del data

                        if not tx_queue.empty():
                            tx_data = tx_queue.get_nowait()
                            client_socket.sendall((tx_data + DATA_END_CHAR).encode('utf-8'))
                            print(f'Sent data: {tx_data}')
                            del tx_data
                        else:
                            # send <IGNORE_MESSAGE> to keep connection
                            client_socket.sendall((IGNORE_DATA + DATA_END_CHAR).encode('utf-8'))

                    except Exception:
                        traceback.print_exc(file=sys.stdout)
                        break

                print(f'Disconnection from : {address}')
                server_status = SERVER_STATUS_DISCONNECTED

    server_status = SERVER_STATUS_STOPPED
    print('server stopping')


def stop_sever():
    global server_status

    server_status = SERVER_STATUS_STOPPED
#     time.sleep(0.5)


def send_data(data):
    global tx_queue

    print(f'tx_size: {tx_queue.qsize()}')

    tx_queue.put_nowait(data)


def receive_data():
    global rx_queue

    if rx_queue.empty():
        return None

    print(f'rx_size: {rx_queue.qsize()}')

    return rx_queue.get_nowait()


def get_server_status():
    return server_status

def is_client_connected():    
    return server_status == SERVER_STATUS_CONNECTED


server_thread = None


def start_server_threaded():
    global server_thread
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()


def stop_server_threaded():
    global server_thread
    stop_sever()

    server_thread.join(timeout=2)
