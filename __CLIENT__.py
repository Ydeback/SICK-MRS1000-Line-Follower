# File for initialization of variables for the client methodset 

import os
import socket
from __MAIN__ import flags

## Configuration parameters for the LiDAR
# Angles in degrees for the data output range, 0 degrees is in the direction
# straight forward in the lidar direction. The start value is set as the
# maximum angle to the right of 0 degrees and the stop value is set as the
# angle to the left of 0 degrees.
startrange = 0
stoprange = 40

## Parameters for activating and specifying the mode of data output from the
## LiDAR
# Data output of remission the corresponding angle (uint_8: 0 (OFF), 1 (RSSI), 8 (AINF), 9 (AINF & RSSI))
remang = b'0'
# Resolution of remission data (enum_8: 0 (8bit), 1 (16-bit))
remres = b'1'
# Position data (bool: 0 (no), 1 (yes))
position = b'0'
# Device name (bool: 0 (no), 1 (yes))
devicename = b'0'
# Comment (bool: 0 (no), 1 (yes))
comment = b'0'
# Time (bool: 0 (no), 1 (yes))
timeinfo = b'0'
# Echo filter (Enum_8: 0 (First echo), 1 (All echos), 2 (Last echo))
echo = b'0'
# Particle filter activation (bool: 0 (Inactive), 1 (Active))
particle = b'1'
# Mean filter activation (bool_1: 0 (Inactive), 1 (Active)) 
mean = b'0'
# Mean filter number of scans (Uint_16: number of scans)
nummean = 2 
# Median filter activation (bool_1: 0 (Inactive), 1 (Active)) 
median = b'0'


##### FIXED #####
# Attribute to represent the buffer size of the communications
BUFFER = 2048
# Fail check flag if the configuration failed in some way --> visuals
flags["CONFIG"] = False
# Tuple to hold the answers from the LiDAR during configuration
config = {}

# IP-address of the server side (LiDAR)
HOST = "192.168.0.1"
# PORT number for the communication with the server side (LiDAR)
PORT = 2112
# Construct the socket address for the server side (LiDAR)
ADDRESS = (HOST, PORT)

# Attribute to represent the timeout time for the socket operations in
# seconds
timeout = 15
