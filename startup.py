# Startup configuration of MRS1000c LiDAR

# ifndef windows
# ifndef linux
# ifndef mac

import socket
from collections import namedtuple as nt

BUFFER = 2064

# Device ip-address
HOST = "169.254.93.123"

# Commication port
PORT = 2112

# Create Address for the device
ADDRESS = (HOST, PORT)

### Variables for the parameter configuration of the LiDAR
# Starting angle in degrees for the data output range
startrange = 15
# Stop angle in degrees for the data output range
stoprange = 15
# Remission and angle (uint_8: 0 (no), 1 (RSSI), 8 (AINF), 9 (RSSI & AINF))
remissionandangle = b'0'
# Resolution of remission data (enum_8: 1 (8bit), 2 (16-bit))
remissionresolution = b'0'
# Position (bool: 0 (no), 1 (yes)))
position = b'0'
# Device name  (bool: 0 (no), 1 (yes)))
devicename = b'0'
# Comment (bool: 0 (no), 1 (yes))
comment = b'0'
# time (bool: 0 (no), 1 (yes))
time = b'0'

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Connect to the LiDAR
def connect():
    try:
        s.connect(ADDRESS)
        print("Connected to:", HOST)
    except socket.error as error:
        print("Connection failed: ", error)
        exit()

def disconnect():
    try:
        s.shutdown
        print("Disconnected from:", HOST)
    except socket.error as error:
        print("Disconnection failed: ", error)
        exit()

# Decimal to hexadecimal conversion
def fromDecToHex(x):
    return bytes(hex(x).split('x')[-1].upper(), encoding='ascii')

# Login as Authorized client
def login():
    s.send(b'\x02sMN SetAccessMode 03 F4724744\x03')
    msg = s.recv(BUFFER)
    return msg

# Set output data range
def setDataRange(startrange, stoprange):
    s.send(b'\x02sWN LMPoutputRange 1 9C4 ' + stop + b' ' + start + b'\x03')
    msg = s.recv(BUFFER)
    return msg

# Read output data range
def readDataRange():
    s.send(b'\x02sRN LMPoutputRange\x03')
    msg = s.recv(BUFFER)
    return msg

# Load factory defaults
def loadFactoryDefaults():
    # s.send(b'\x02sMN mSCloadfacdef\x03')
    # msg = s.recv(BUFFER)
    # return msg
    pass

# Set data stream contents
def setDataContent():
    s.send(
        b'\x02sWN LMDscandatacfg 00 00 ' + remissionandangle + b' ' + remissionresolution + b' 0 0 0 ' + position + b' ' + devicename + b' ' + comment + b' ' + time + b' 01\x03')
    msg = s.recv(BUFFER)
    return msg

# Read device status (Ready, logged-in, error)
def readDeviceStatus():
    s.send(b'\x02sRN SCdevicestate\x03')
    msg = s.recv(BUFFER)
    return msg

# Store configuration permanently
def storePermanently():
    s.send(b'\x02sMN mEEwriteall\x03')
    msg = s.recv(BUFFER)
    return msg

## Unit and encoding changes for the parameter variables
stop = fromDecToHex((90 - startrange) * 10000)
start = fromDecToHex((90 + stoprange) * 10000)

# Loading the config of the MRS1000c LiDAR
def loadconfig():
    NamedTuple = nt("Answers",
                    ["Login", "SetDataRange", "ReadDataRange", "ReadAngleAndFrequency", "LoadFactoryDefaults",
                     "SetDataContent", "SetToStandby", "RebootDevice", "ReadDeviceStatus", "StorePermanently",
                     "StartMeas", "StopMeas"])

    header = {}
    header["Login"] = login()
    header["ReadDataRange"] = readDataRange()
    if header["ReadDataRange"] != b'\x02sWA LMPoutputRange\x03':
        header["SetDataRange"] = setDataRange(startrange, stoprange)
    header["SetDataContent"] = setDataContent()
    # header["RebootDevice"] = rebootDevice()
    header["StorePermanently"] = storePermanently()
    header["ReadDeviceStatus"] = readDeviceStatus()
    # header["LoadFactoryDefaults"] = loadFactoryDefaults()

    return header


# Check if all the config settings has been set successfully
def failCheckfunc(header):
    if header["Login"] != b'\x02sAN SetAccessMode 1\x03':
        return True
    elif header["SetDataRange"] != b'\x02sWA LMPoutputRange\x03':
        return True
    elif header["SetDataContent"] != b'\x02sWA LMDscandatacfg\x03':
        return True
    elif header["ReadDeviceStatus"] == b'\x02sRA SCdevicestate 2\x03':
        return True
    elif header["StorePermanently"] == b'\x02sAN mEEwriteall 0\x03':
        return True
    else:
        return False


def failCheck(header):
    if failCheckfunc(header):
        print("Startup Configuration failed!")
    else:
        print("All configurations was set successfully!")


# Send data request message
def run():
    s.send(b'\x02sEN LMDscandata 1\x03\0')
    print("Retreiving position data!...")
    trash = s.recv(BUFFER)
