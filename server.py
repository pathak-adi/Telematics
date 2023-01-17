import socket
import threading
import requests
import json
from websocket import create_connection
import codec8e
import pandas as pd

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind(ADDR)
except:
    print('reusing socket address')
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(ADDR)


def handle_client(connection, address):
    print(f" New Connection: {address} has connected")
    connected = True
    msg = connection.recv(1024)
    msg = msg.decode(FORMAT)
    print(msg)
    device_imei = msg  # bytes.fromhex(msg[4:])
    send_data_ws(0, device_imei)
    print(f"f [{address, PORT}]: {device_imei}")
    connection.send(bytes.fromhex('01'))
    # connection.send(ba)
    while connected:
        msg = connection.recv(1024).hex()
        if len(msg) > 0:
            # msg = connection.recv(1024).decode(FORMAT)
            msg = str(msg)

            if msg == DISCONNECT_MESSAGE:
                connected = False
                print('disconnecting')
                connection.send(b'00')
            else:
                print(f"{address} {msg}")
                response = parse_avl_packet(msg, device_imei)
                connection.send(bytes.fromhex(response))
    connection.close()


def start():
    server.listen()
    print(f" [LISTENTING] Server is listening on {SERVER}")
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(connection, address))
        thread.start()
        print(f"Active Connections: {threading.active_count() - 1}")


def parse_avl_packet(data, imei):
    try:
        zero_bytes = data[:8]
        data_field_length = data[8:16]
        codec_id = data[16:18]
        num_records = data[18:20]
        records, device_timestamp = codec8e.codec_8e(data[20:], int(num_records, 16))
        save_data(imei, records, device_timestamp)
    except:
        records = ['Error']
        num_records = 0

    send_data_ws(imei, records)
    # send_data(item)
    return '000000' + num_records


def reconnect():
    ws = create_connection("wss://degjo0ipsa.execute-api.us-east-1.amazonaws.com/production")


def save_data(imei, records,timestamp):
    url = 'https://94bup2tdy0.execute-api.us-east-1.amazonaws.com/production/data/append'
    body = {
        "datetime": timestamp,
        "imei": f"FMB640_{imei}",
        "data": records
    }

    resp = requests.post(url, json.dumps(body))
    return resp


def send_data_ws(imei, records):
    try:
        item = {
            "action": "sendMessage",
            "data": json.dumps(records)

        }
        ws.send(json.dumps(item))
    except:
        ws.close()
        reconnect()

    return 0


def send_data(data):
    url = f'https://z92bvmqd7b.execute-api.us-east-1.amazonaws.com/staging/impact_metrics/create'
    qs = requests.post(url, json.dumps(data))
    # Add sorting by date
    print(qs.json())
    return 0


def send_init(data):
    url = f'https://z92bvmqd7b.execute-api.us-east-1.amazonaws.com/staging/impact_metrics/create'
    item = {
        'city': data,
        'operating_mileage': 'none',
        'co2_mitigated': 'none',
        'diesel_avoided': 'none',
        'passengers_carried': 'none',
    }
    qs = requests.post(url, json.dumps(item))
    # Add sorting by date
    print(qs.json())
    return 0


print("[STARTING] Server is starting")

if __name__ == "__main__":
    ws = create_connection("wss://degjo0ipsa.execute-api.us-east-1.amazonaws.com/production")
    start()
