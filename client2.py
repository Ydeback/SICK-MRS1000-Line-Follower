import socket
import math
import numpy as np

HOST = "169.254.93.123"
PORT = 2112
ADDRESS = (HOST,PORT)

def parse_number(data):
    if b'+' in data or b'-' in data:
        return int(data)
    else:
        return int(data, 16)

def layercheck(data):
    if data == b'FE0C':
        print("Layer: 4")
    elif data == b'FF06':
        print("Layer: 3")
    elif data == b'0':
        print("Layer: 2")
    elif data == b'FA':
        print("Layer: 1")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Socket created")

    try:
        s.connect(ADDRESS)
        print("Connected to:", HOST)
    except socket.error:
        print("Connection failed")

    msg = b'\x02sEN LMDscandata 1\x03\0'
    s.send(msg)
    while True:

        data = s.recv(2048)
        print('ASCII:', data)

        if len(data) < 30: #Ignorera första strängen som skickas
            continue
        else:
            data = data.split(b' ')
            number = parse_number(data[25])
            layercheck(data[15])
            print('Number points:', number)
            dist = [parse_number(x) / 1000 for x in data[26:26+number]]
            print('Distance [m]:', dist)

            arr = np.array(dist)  #gör om dist listan till array

            #Filter som sätter allt efter ett visst avstånd till 0
            high_threshold = 2.5
            low_threshold = 0.5

            arr[arr > high_threshold] = 99
            arr[arr < low_threshold] = 99
            print(arr)

            index = np.where(arr == np.amin(arr)) #hitta index för det minimala eller maximala avståndet
            #print(index)
            print(arr[index[0]])

            #skala mätpunkterna utifrån vinklarna.
            angle = np.linspace(0.08726646259, -0.08726646259, number)
            print(angle[index[0]])

            #Beräkna position i sidled
            x = np.sin(angle)
            #print(x[index])
            pos = np.multiply(x[index],arr[index[0]])
            print(pos)