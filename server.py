import socket
import threading
import os

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(connection, address):
    print(f" New Connection: {address} has connected")
    connected = True
    while connected:
        msg_length = connection.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = connection.recv(msg_length).decode(FORMAT)
            print(f"f [{address}]: {msg}")
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"{address} {msg}")
    connection.close()


def start():
    server.listen()
    print(f" [LISTENTING] Server is listening on {SERVER}")
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(connection, address))
        thread.start()
        print(f"Active Connections: {threading.active_count() - 1}")


print("[STARTING] Server is starting")
if __name__ == "__main__":
    start()
