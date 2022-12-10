import socket
import threading
import requests
import json
from datetime import datetime

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
    print(msg)
    msg = msg.decode(FORMAT)
    print(msg)
    device_imei = msg  # bytes.fromhex(msg[4:])
    send_init(device_imei)
    print(f"f [{address, PORT}]: {device_imei}")
    connection.send(bytes.fromhex('01'))
    # connection.send(ba)
    while connected:
        msg = connection.recv(1024).hex()
        # msg = connection.recv(1024).decode(FORMAT)
        print(msg)
        msg = str(msg)

        if msg == DISCONNECT_MESSAGE:
            connected = False
            print('disconnecting')
            connection.send(b'00')
        else:
            print(f"{address} {msg}")
            response = parse_avl_packet(msg)
            print(response)
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


def parse_avl_packet(data):
    zero_bytes = data[:8]
    data_field_length = data[8:16]
    codec_id = data[16:18]
    num_records = data[18:20]
    time_stamp = data[20:36]
    priority = data[36:38]
    try:
        speed = int(data[64:68], 16)
        lon = int(data[38:46], 16)
        lat = int(data[46:54], 16)
        if lat >= 90000000:
            lat = lat - 2 ** 32
        if lon >= 180000000:
            lon = lon - 2 ** 32
        gps = {
            "longitude": str(lon/10000000),
            "latitude": str(lat/10000000),
            "altitude": str(int(data[54:58], 16)),
            "angle": str(int(data[58:62],16)),
            "satellites": str(int(data[62:64],16)),
            "gps_speed": str(speed)
        }
    except:
        gps = {
            "longitude": data[38:46],
            "latitude": data[46:54],
            "altitude": data[54:58],
            "angle": data[58:62],
            "satellites": data[62:64],
            "gps_speed": data[64:68]
        }
        lat,lon = 0,0
        speed = 0

    print(f'zero_bytes {zero_bytes}')
    print(f'data_field {data_field_length}')
    print(f'codec {codec_id}')
    print(f'records {num_records}')
    print(f'timestamp {time_stamp}')
    print(f'gps {gps}')
    try:
        t = int(time_stamp, 16)
        time_stamp = datetime.utcfromtimestamp(t / 1000).strftime('%Y-%m-%d %H:%M:%S')
    except:
        pass

    item = {
        'city': time_stamp,
        'operating_mileage': gps,
        'co2_mitigated': str(speed),
        'diesel_avoided': data,
        'passengers_carried': f'{lat} | {lon}',
    }
    send_data(item)
    return '000000' + num_records


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
    start()
