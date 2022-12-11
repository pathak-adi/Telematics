from datetime import datetime

avl = {239: 'Ignition',
       240: 'Movement',
       22: 'Data Mode',
       21: 'GSM Signal',
       200: 'Sleep Mode',
       71: 'GNSS Status',
       181: 'GNSS PDOP',
       182: 'GNSS HDOP',
       66: 'External Voltage',
       24: 'Speed',
       205: 'GSM Cell ID',
       206: 'GSM Area Code',
       67: 'Battery Voltage',
       68: 'Battery Current',
       241: 'Active GSM Operator',
       199: 'Trip Odometer',
       216: 'Total Odometer',
       1: 'Digital Input 1',
       9: 'Analog Input 1',
       179: 'Digital Output 1',
       236: 'Axis X',
       237: 'Axis Y',
       238: 'Axis Z',
       219: 'CCID Part1',
       220: 'CCID Part2',
       221: 'CCID Part3',
       144: 'SD Status',
       2: 'Digital Input 2',
       3: 'Digital Input 3',
       10: 'Analog Input 2',
       180: 'Digital Output 2',
       72: 'Dallas Temperature 1',
       73: 'Dallas Temperature 2',
       74: 'Dallas Temperature 3',
       75: 'Dallas Temperature 4',
       62: 'Dallas Temperature ID 1',
       63: 'Dallas Temperature ID 2',
       64: 'Dallas Temperature ID 3',
       65: 'Dallas Temperature ID 4',
       78: 'iButton',
       76: 'Fuel Counter',
       10640: 'Impulse counter frequency 1',
       10641: 'Impulse counter RPM 1',
       483: 'Impulse Counter 2',
       10642: 'Impulse counter frequency 2',
       10643: 'Impulse counter RPM 2',
       207: 'RFID',
       201: 'LLS 1 Fuel Level',
       202: 'LLS 1 Temperature',
       203: 'LLS 2 Fuel Level',
       204: 'LLS 2 Temperature',
       210: 'LLS 3 Fuel Level',
       211: 'LLS 3 Temperature',
       212: 'LLS 4 Fuel Level',
       213: 'LLS 4 Temperature',
       214: 'LLS 5 Fuel Level',
       215: 'LLS 5 Temperature',
       178: 'Network Type',
       108: 'Number Of Records',
       4: 'Digital Input 4',
       50: 'Digital Output 3',
       51: 'Digital Output 4',
       11: 'Analog Input 3',
       245: 'Analog Input 4',
       70: 'PCB Temperature',
       5: 'Dallas Temperature ID 5',
       6: 'Dallas Temperature 5',
       7: 'Dallas Temperature ID 6',
       8: 'Dallas Temperature 6',
       217: 'RFID COM2',
       218: 'IMSI',
       224: 'Ultrasonic Fuel Level 1',
       225: 'Ultrasonic Fuel Level 2',
       208: 'Ultrasonic Software Status 1',
       209: 'Ultrasonic Software Status 2',
       484: 'External Sensor Temperature 1',
       485: 'External Sensor Temperature 2',
       486: 'External Sensor Temperature 3',
       487: 'External Sensor Temperature 4',
       488: 'External Sensor Temperature 5',
       489: 'External Sensor Temperature 6',
       701: 'BLE 1 temperature',
       702: 'BLE 2 temperature',
       703: 'BLE 3 temperature',
       704: 'BLE 4 temperature',
       705: 'BLE 1 Battery Voltage',
       706: 'BLE 2 Battery Voltage',
       707: 'BLE 3 Battery Voltage',
       708: 'BLE 4 Battery Voltage',
       709: 'BLE 1 Humidity',
       710: 'BLE 2 Humidity',
       711: 'BLE 3 Humidity',
       712: 'BLE 4 Humidity',
       713: 'BLE Sensor Custom 1',
       714: 'BLE Sensor Custom 2',
       715: 'BLE Sensor Custom 3',
       716: 'BLE Sensor Custom 4',
       717: 'BLE Luminosity 1',
       718: 'BLE Luminosity 2',
       719: 'BLE Luminosity 3',
       720: 'BLE Luminosity 4',
       721: 'BLE LLS Fuel 1',
       722: 'BLE LLS Fuel 2',
       723: 'BLE LLS Fuel 3',
       724: 'BLE LLS Fuel 4',
       725: 'BLE Frequency 1',
       726: 'BLE Frequency 2',
       727: 'BLE Frequency 3',
       728: 'BLE Frequency 4',
       729: 'BLE Sensor Custom 12',
       730: 'BLE Sensor Custom 13',
       731: 'BLE Sensor Custom 14',
       732: 'BLE Sensor Custom 15',
       733: 'BLE Sensor Custom 22',
       734: 'BLE Sensor Custom 23',
       735: 'BLE Sensor Custom 24',
       736: 'BLE Sensor Custom 25',
       737: 'BLE Sensor Custom 32',
       738: 'BLE Sensor Custom 33',
       739: 'BLE Sensor Custom 34',
       740: 'BLE Sensor Custom 35',
       741: 'BLE Sensor Custom 42',
       742: 'BLE Sensor Custom 43',
       743: 'BLE Sensor Custom 44',
       744: 'BLE Sensor Custom 45',
       10009: 'Eco score',
       10487: '1Wire Humidity 1',
       10488: '1Wire Humidity 2',
       10489: '1Wire Humidity 3',
       10490: '1Wire Humidity 4',
       10491: '1Wire Humidity 5',
       10492: '1Wire Humidity 6',
       79: 'Brake Switch',
       80: 'Wheel Based Speed',
       81: 'Cruise Control Active',
       82: 'Clutch Switch',
       83: 'PTO State',
       84: 'Acceleration Pedal Position',
       85: 'Engine Current Load',
       86: 'Engine Total Fuel Used',
       87: 'Fuel Level',
       88: 'Engine Speed',
       89: 'Axle weight 1',
       90: 'Axle weight 2',
       91: 'Axle weight 3',
       92: 'Axle weight 4',
       93: 'Axle weight 5',
       94: 'Axle weight 6',
       95: 'Axle weight 7',
       96: 'Axle weight 8',
       97: 'Axle weight 9',
       98: 'Axle weight 10',
       99: 'Axle weight 11',
       100: 'Axle weight 12',
       101: 'Axle weight 13',
       102: 'Axle weight 14',
       103: 'Axle weight 15',
       104: 'Engine Total Hours Of Operation',
       109: 'Software Version Supported',
       110: 'Diagnostics Supported',
       111: 'Requests Supported',
       113: 'Service Distance',
       122: 'Direction Indication',
       123: 'Tachograph Performance',
       124: 'Handling Info',
       125: 'System Event',
       127: 'Engine Coolant Temperature',
       128: 'Ambient Air Temperature',
       135: 'Fuel Rate',
       136: 'Instantaneous Fuel Economy',
       137: 'PTO Drive Engagement',
       138: 'High Resolution Engine Total Fuel Used',
       139: 'Gross Combination Vehicle Weight',
       229: 'AdBlue status',
       357: 'Brake Pedal Position',
       10348: 'Fuel level 2',
       10349: 'MIL indicator',
       10428: 'Tell Tale 0',
       10429: 'Tell Tale 1',
       10430: 'Tell Tale 2',
       10431: 'Tell Tale 3'}


def codec_8e(data, num_records):
    n_max = len(data)
    nx = 0
    records = []
    for nr in range(num_records):
        print(nr)
        time_stamp = data[0:16]
        t = int(time_stamp, 16)
        time_stamp = datetime.utcfromtimestamp(t / 1000).strftime('%Y-%m-%d %H:%M:%S')
        priority = data[16:18]
        lon = int(data[18:26], 16)
        lat = int(data[26:34], 16)
        speed = int(data[44:48], 16)
        if lat >= 850000000:
            lat = lat - 2 ** 32
        if lon >= 1800000000:
            lon = lon - 2 ** 32

        gps = {
            "timestamp": time_stamp,
            "longitude": str(lon / 10000000),
            "latitude": str(lat / 10000000),
            "altitude": str(int(data[34:38], 16)),
            "angle": str(int(data[38:42], 16)),
            "satellites": str(int(data[42:44], 16)),
            "gps_speed": str(speed)
        }

        n = 48
        event_io_id = data[n:n + 4]
        n += 4
        n_total_io = data[n:n + 4]
        n += 4

        # 1 byte io
        n_1_io = data[n:n + 4]
        n += 4
        num_byte_1 = int(n_1_io, 16)  # number of properties of length 1 byte
        avl_id_1_byte = []
        avl_id_1_value = []
        avl_id_2_byte = []
        avl_id_2_value = []
        avl_id_4_byte = []
        avl_id_4_value = []
        avl_id_8_byte = []
        avl_id_8_value = []
        avl_id_x_byte = []
        avl_id_x_value = []
        for i in range(0, num_byte_1):
            n_id_1 = data[n:n + 4]
            n += 4
            n_value_1 = data[n:n + 2]
            n += 2
            avl_id_1_byte.append(avl_id(int(n_id_1, 16)))
            avl_id_1_value.append(int(n_value_1, 16))

        num_byte_2 = int(data[n:n + 4], 16)  # number of properties of length 2 bytes
        n += 4
        for i in range(0, num_byte_2):
            n_id_2 = data[n:n + 4]
            n += 4
            n_value_2 = data[n:n + 4]
            n += 4
            avl_id_2_byte.append(avl_id(int(n_id_2, 16)))
            avl_id_2_value.append(int(n_value_2, 16))

        num_byte_4 = int(data[n:n + 4], 16)  # number of properties of length 4 bytes
        n += 4
        for i in range(0, num_byte_4):
            n_id_4 = data[n:n + 4]
            n += 4
            n_value_4 = data[n:n + 8]
            n += 8
            avl_id_4_byte.append(avl_id(int(n_id_4, 16)))
            avl_id_4_value.append(int(n_value_4, 16))

        num_byte_8 = int(data[n:n + 4], 16)  # number of properties of length 8 bytes
        n += 4
        for i in range(0, num_byte_8):
            n_id_8 = data[n:n + 4]
            n += 4
            n_value_8 = data[n:n + 16]
            n += 16
            avl_id_8_byte.append(avl_id(int(n_id_8, 16)))
            avl_id_8_value.append(int(n_value_8, 16))

        num_byte_x = int(data[n:n + 4], 16)  # number of properties of length x bytes
        n += 4
        for i in range(0, num_byte_x):
            n_id_x = data[n:n + 4]
            n += 4
            n_id_len = int(data[n:n + 4], 16)
            n += 4
            n_value_x = data[n:(n + (n_id_len * 2))]
            n += (n_id_len * 2)
            avl_id_x_byte.append(avl_id(int(n_id_x, 16)))
            avl_id_x_value.append(int(n_value_x, 16))
        data = data[n:]
        nx += n
        avl_ids = avl_id_1_byte + avl_id_2_byte + avl_id_4_byte + avl_id_8_byte + avl_id_x_byte
        avl_value = avl_id_1_value + avl_id_2_value + avl_id_4_value + avl_id_8_value + avl_id_x_value
        record = dict(zip(avl_ids, avl_value))

        record = record | gps
        records.append(record)
        print(records)

    return records


def avl_id(id):
    try:
        resp = avl[id]
        resp = f'{resp}_{id}'
    except:
        resp = id
    return resp


# data="00000000000001868e" \
#      "03" \
if __name__ == "__main__":
    data = "00000184ff53895a0015fc63f8ff3a8e2b066a008d13002300000013000700320000160100470300f00100150500c80000ef01000500b5000900b6000500426b060018ffff00bfffff000500c70000000000d80000000000c2639554df00c0ffffffff00c1ffffffff00020091ffffffffffffffff00927e00000000000000000000000184ff5385720015fc61c1ff3a90e7066b009712002300000013000700320000160100470300f00100150500c80000ef01000500b5000900b6000500426b190018ffff00bfffff000500c70000000000d80000000000c2639554de00c0ffffffff00c1ffffffff00020091ffffffffffffffff00927e00000000000000000000000184ff53277f0015fc42d4ff3b1d98066300a612004000000013000700320000160100470300f00100150500c80000ef01000500b5000b00b6000500426af50018ffff00bfffff000500c70000000000d80000000000c2639554c600c0ffffffff00c1ffffffff00020091ffffffffffffffff00927e00000000000000000003000006ef"
    codec_8e(data, 3)
