import socket
import time

HOST = "169.254.93.123"
PORT = 2112
ADDRESS = (HOST,PORT)

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    print("Socket created")

    try:
        s.connect(ADDRESS)
        print("Connected to:",HOST)
    except socket.error:
        print("Connection failed")

    msg = b'\x02sRN LMDscandata 1\x03\0'

    while True:
        s.send(msg)
        data = s.recv(2048)
        print("data received")
        print(data)
        time.sleep(3)



