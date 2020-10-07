import socket
import time
import numpy as np

HOST = "169.254.93.123"
PORT = 2112
ADDRESS = (HOST,PORT)

def parse_number(data):
    if b'+' in data or b'-' in data:
        return int(data)
    else:
        return int(data,16)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Socket created")

    try:
        s.connect(ADDRESS)
        print("Connected to:", HOST)
    except socket.error:
        print("Connection failed")

    msg = b'\x02sRN LMDscandata 1\x03\0'

    while True:
        s.send(msg)
        data = s.recv(2048)
        print("data received")
        
        data = data.split(b' ')
        number = parse_number(data[25]) 
        print(number)   
        dist = [parse_number(x) / 1000 for x in data[26:26+number]]
        print(dist)
        angle = np.linspace(0.08726646259, -0.08726646259, number)
        print(angle)
        time.sleep(3)
        


