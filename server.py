import socket
import threading
import requests
import json

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
    msg = connection.recv(1024).decode(FORMAT)
    print(msg)
    device_imei = bytes.fromhex(msg[4:])
    send_init(device_imei)
    print(f"f [{address, PORT}]: {device_imei}")
    # connection.send(b'0x01')
    ba=bytearray()
    ba.append(1)
    connection.send(ba)
    while connected:
        msg = connection.recv(1024).decode(FORMAT)
        msg=str(msg)


        if msg == DISCONNECT_MESSAGE:
            connected = False
            print('disconnecting')
            connection.send(b'00')
        else:
            print(f"{address} {msg}")
            response=parse_avl_packet(msg)
            print(response)
            connection.send(response)
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
    zero_bytes=data[:8]
    data_field_length=data[8:16]
    codec_id=data[16:18]
    num_records=data[18:20]
    time_stamp=data[20:36]
    priority=data[36:38]
    gps={
        "longitude":data[38:46],
        "latitude":data[46:54],
        "altitude":data[54:58],
        "angle":data[58:62],
        "satellites":data[62:64],
        "gps_speed":data[64:68]
    }

    print(f'zero_bytes {zero_bytes}')
    print(f'data_field {data_field_length}')
    print(f'codec {codec_id}')
    print(f'records {num_records}')
    print(f'timestamp {int(time_stamp,16)}')
    print(f'gps {gps}')
    item={
        'city':time_stamp,
        'operating_mileage':gps,
        'co2_mitigated': data_field_length,
        'diesel_avoided': data,
        'passengers_carried': priority,
    }
    send_data(item)
    return b'00'+bytes(num_records, 'utf-8')


def send_data(data):
    url=f'https://z92bvmqd7b.execute-api.us-east-1.amazonaws.com/staging/impact_metrics/create'
    qs = requests.post(url,json.dumps(data))
    # Add sorting by date
    print(qs.json())
    return 0
def send_init(data):
    url=f'https://z92bvmqd7b.execute-api.us-east-1.amazonaws.com/staging/impact_metrics/create'
    item={
         'city':data,
        'operating_mileage':'none',
        'co2_mitigated': 'none',
        'diesel_avoided': 'none',
        'passengers_carried': 'none',
    }
    qs = requests.post(url,json.dumps(data))
    # Add sorting by date
    print(qs.json())
    return 0

print("[STARTING] Server is starting")
if __name__ == "__main__":
    start()
