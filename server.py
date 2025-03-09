import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

thread_end_flags = {}

def handle_client(conn, addr, i):
    file_name = addr[0].replace('.', '_')
    thread_end_flags[f"t{i}_end"] = False  

    while not thread_end_flags[f"t{i}_end"]:  
        try:
            msg = conn.recv(2048).decode()
            if not msg:  
                break
            with open(file_name, 'a') as file:
                file.write(msg)
        except:
            break

    
    thread_end_flags[f"t{i}_end"] = True
    conn.close()

def disc_usr():
    while True:
        ip = input("Enter the IP to disconnect: ")
        index = None
        for k, v in client_list.items():
            if v == ip:
                index = k
                break
        if index:
            thread_end_flags[index] = True
            print(f"Client with IP {ip} disconnected.")
        else:
            print(f"No client found with IP {ip}.")

i = 1
client_list = {}  
threads = {}

def start():
    t0 = threading.Thread(target=disc_usr, daemon=True)
    t0.start()

    server.listen()
    global i
    while True:
        conn, addr = server.accept()
        client_list[f"t{i}"] = f"{addr[0]}"  

        thread = threading.Thread(target=handle_client, args=(conn, addr, i))
        threads[f"t{i}"] = thread
        thread.start()
        i += 1

if __name__ == "__main__":
    start()
