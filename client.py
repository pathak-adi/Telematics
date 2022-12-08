import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
SERVER = "172.19.16.1"
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDRESS = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    padded_send_length = send_length
    send_length += b' '*(HEADER- len(send_length))
    client.send(send_length)
    client.send(message)

send("Hello Adi!")
send("Hello Adi!")
send("Hello Adi!")
send(DISCONNECT_MESSAGE)