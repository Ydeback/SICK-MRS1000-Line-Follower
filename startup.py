#Startup configuration of MRS1000c LiDAR

#ifndef windows
#ifndef linux
#ifndef mac

import socket

# Device ip-address
HOST = "169.254.93.123" 

# Commication port
PORT = 2112

# Create Address for the device
ADDRESS = (HOST,PORT) 

# Temporary value of start angle (horz)(rad)
START_ANGLE = 0.08726646259 

# Temporary value of stop angle (horz)(rad)
STOP_ANGLE = -0.08726646259 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the LiDAR
def connect(): 
    try:
        s.connect(ADDRESS)
        print("Connected to:", HOST)
    except socket.error as error:
        print("Connection failed: ", error)
        exit()

# Loading the config of the MRS1000c LiDAR 
def load_config():
    # s.send(b'\x02sMN SetAccessMode 03 F4724744\x03')
    pass

def run():
    s.send(b'\x02sEN LMDscandata 1\x03\0')
    print("Message sent")
# Load config and connect to LiDAR
def startup(): 
    connect()
    load_config()
    run()