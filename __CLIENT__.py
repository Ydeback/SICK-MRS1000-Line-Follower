# File for initialization of variables for the client methodset 

import os
import socket
from __INIT__ import *

## Configuration parameters for the LiDAR
# Angles in degrees for the data output range
startrange = 10
stoprange = 10
# Remission and angle (uint_8: 0 (no), 1 (RSSI), 8 (AINF), 9 (AINF & RSSI))
remang = b'0'
# Resolution of remission data (enum_8: 1 (8bit), 1 (16-bit))
remres = b'0'
# Position data (bool: 0 (no), 1 (yes))
position = b'0'
# Device name (bool: 0 (no), 1 (yes))
devicename = b'0'
# Comment (bool: 0 (no), 1 (yes))
comment = b'0'
# Time (bool: 0 (no), 1 (yes))
timeinfo = b'0'
# Echo filter (Enum_8: 0 (First echo), 1 (All echos), 2 (Last echo))
echo = b'1'
# Particle filter activation (bool_1: 0 (Inactive), 1 (Active))
particle = b'1'
# Particle size threshold (Uint_16: particle size (mm))
particlesize = 4
# Mean filter activation (bool_1: 0 (Inactive), 1 (Active)) 
mean = b'1'
# Mean filter number of scans (Uint_16: number of scans)
nummean = 2 
# Median filter activation (bool_1: 0 (Inactive), 1 (Active)) 
median = b'1'


##### FIXED #####
# Fail check flag if the configuration failed in some way --> visuals
flags["CONFIG"] = False

# IP-address of the server side (LiDAR)
HOST = "192.168.0.1"
# PORT number for the communication with the server side (LiDAR)
PORT = 2112
# Construct the socket address for the server side (LiDAR)
ADDRESS = (HOST, PORT)

# Attribute to represent the timeout time for the socket operations in
# seconds
timeout = 5
