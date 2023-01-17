import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
SERVER = '34.195.164.232'#'34.225.168.50' #"172.19.16.1"#'
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
    # client.send(send_length)
    print(message)
    client.send(message)
    resp=client.recv(128).decode(FORMAT)

    return resp



if __name__ == "__main__":
    resp=send("000F333536333037303432343431303133")
    # resp=1
    # #resp=int(ord(resp),0)
    # tw="00000000000001868e0300000184ff53cda60015fc99beff3a74c7066500ab12001800000013000700320000160100470300f00100150500c80000ef01000500b5000b00b6000500426b020018ffff00bfffff000500c70000000000d80000000000c2639554f000c0ffffffff00c1ffffffff00020091ffffffffffffffff00927e00000000000000000000000184ff4f95670015fb9ef6ff3e170d0650009f13000d00000013000700320000160100470300f00100150500c80000ef01000500b5000b00b6000500426afe0018ffff00bfffff000500c70000000000d80000000000c2639553dc00c0ffffffff00c1ffffffff00020091ffffffffffffffff00927e00000000000000000000000184ff4f85cb0015fb9dcaff3e1d6e064f00ad13001400000013000700320000160100470300f00100150500c80000ef01000500b5000b00b6000500426b030018ffff00bfffff000500c70000000000d80000000000c2639553d800c0ffffffff00c1ffffffff00020091ffffffffffffffff00927e0000000000000000000300003026"
    # #tw="00000000000001898E0300000184EE89E71B0015FDA6B0FF352A380671013B0C000000FA0014000800320000160000470300F00000150500C80000EF0000FA00000500B5000B00B600070042649D0018FFFF00BFFFFF000500C70000000000D80000000000C2639108AD00C0FFFFFFFF00C1FFFFFFFF00020091FFFFFFFFFFFFFFFF0092FFFFFFFFFFFFFFFF000000000184EE88FC070015FDA6B0FF352A3806"
    #
    # if resp == 1:
    #     send(
    #          tw
    #        # "000000000000004A8E010000016B412CEE000100000000000000000000000000000000010005000100010100010011001D00010010015E2C880002000B000000003544C87A000E000000001DD7E06A00000100002994"
    #     )
    print(resp)
    #send(DISCONNECT_MESSAGE)