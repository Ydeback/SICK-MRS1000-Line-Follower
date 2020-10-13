# Client for connecting to the device and receiving data

import socket
from calculate import *
import numpy as np

HOST = "169.254.93.123"
PORT = 2112
ADDRESS = (HOST, PORT)
MRS1000_START_ANGLE = 0.08726646259
MRS1000_STOP_ANGLE = -0.08726646259

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket created")

# Connect
try:
    s.connect(ADDRESS)
    print("Connected to :",HOST)
except socket.error:
    print("Connection failed")

def run(socket): # Start reading the data
    msg = b'\x02sEN LMDscandata 1\x03\0' 
    s.send(msg)

