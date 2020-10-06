import socket

HOST = "169.254.93.123"
PORT = 2112
ADDRESS = (HOST, PORT)
BUFFER = 64
FORMAT = 'ascii'

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    print("Socket created")

    # Connect
    try:
        s.connect(ADDRESS)
        print("Connected to :",HOST)
    except socket.error:
        print("Connection failed")

    msg = b'\x02sEN LMDscandata 1\x03\0' 
    s.send(msg)
    # Receive data
    while True:
        data = s.recv(BUFFER)



