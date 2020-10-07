import socket
from calculate import *
import numpy as np

HOST = "169.254.93.123"
PORT = 2112
ADDRESS = (HOST, PORT)
BUFFER = 64
FORMAT = 'ascii'
MRS1000_START_ANGLE = 0.08726646259
MRS1000_STOP_ANGLE = -0.08726646259

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
    
    data = from_socket(s)

    # Receive data
    while True:
        datagram = next(data)
        decoded_data = decode_datagram(datagram)

            print(np.linspace(MRS1000_START_ANGLE, MRS1000_STOP_ANGLE,
                len(decoded_data['Data']))
        print(decoded_data)

        if decoded_data is not None:
            node.publish('/lidar/radius', decoded['Data'])
            node.publish('/lidar/theta', np.linspace(TIM561_START_ANGLE, TIM561_STOP_ANGLE, len(decoded['Data'])).tolist())

        

