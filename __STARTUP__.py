# File for initialization of variables for the startup class 

import socket
from collections import namedtuple as nt

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

##### FIXED #####
# Fail check flag if the configuration failed in some way --> visuals
configflag = False
# Connection flag if the connection to the server side (LiDAR) failed
connectflag = False

# def getIP():
    # import subprocess
    # process = subprocess.Popen('sudo arp -D -n -i eth0', shell=True,
            # stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    # stdout, stderr = process.communicate()
    # ans = stdout.split()
    # return ans[6]


# IP-address of the server side (LiDAR)
HOST = "169.254.247.100"
# PORT number for the communication with the server side (LiDAR)
PORT = 2112
# Construct the socket address for the server side (LiDAR)
ADDRESS = (HOST, PORT)
