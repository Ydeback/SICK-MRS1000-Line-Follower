# Client configuration of MRS1000c LiDAR

from __CLIENT__ import *
from __INIT__ import *
from visuals import loadingbar
from visuals import rebootvisual
# Construction of a socket object (TCP)
def createSocket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server side (LiDAR)
def connect(s):
    try:
        s.connect(ADDRESS)
        print("Connected")
    except:
        flags["CONNECT"] = True

# Login as Authorized client
def login(s):
    try:
        s.send(b'\x02sMN SetAccessMode 03 F4724744\x03')
    except socket.error as err:
        flags["LOGIN"]
    return s.recv(BUFFER)


def fromDecToHex(x):
    return bytes(hex(x).split('x')[-1].upper(), encoding='ascii')


# Set output data range
def setDataRange(s, startrange, stoprange):
    s.send(b'\x02sWN LMPoutputRange 1 9C4 ' + stop + b' ' + start + b'\x03')
    trash = s.recv(BUFFER)

# Read output data range
def readDataRange(s):
    s.send(b'\x02sRN LMPoutputRange\x03')
    return s.recv(BUFFER)

# Configure the data output content
def setDataContent(s):
    s.send(
        b'\x02sWN LMDscandatacfg 00 00 ' + remang  + b' ' + remres + b' 0 0 0 '
        + position + b' ' + devicename + b' ' + comment + b' ' + timeinfo + b' 01\x03')
    return s.recv(BUFFER)

def setEchoFilter(s):
    s.send(b'\x02sWN FREchoFilter ' + echo + b'\x03')
    trash = s.recv(BUFFER)

# Read device status (Ready, logged-in, error)
def readDeviceStatus(s):
    s.send(b'\x02sRN SCdevicestate\x03')
    return s.recv(BUFFER)


# Store configuration permanently
def storePermanently(s):
    s.send(b'\x02sMN mEEwriteall\x03')
    return s.recv(BUFFER)


## Unit and encoding changes for the parameter variables
stop = fromDecToHex((90 - startrange) * 10000)
start = fromDecToHex((90 + stoprange) * 10000)

# Loading the config of the MRS1000c LiDAR
def loadconfig(s):
    NamedTuple = nt("Answers",
                    ["Login", "SetDataRange", "ReadDataRange", "ReadAngleAndFrequency", "LoadFactoryDefaults",
                     "SetDataContent", "SetToStandby", "RebootDevice", "ReadDeviceStatus", "StorePermanently",
                     "StartMeas", "StopMeas"])

    header = {}
    header["Login"] = login(s)
    header["ReadDataRange"] = readDataRange(s)
    if header["ReadDataRange"] != b'\x02sWA LMPoutputRange\x03':
        header["SetDataRange"] = setDataRange(s,startrange, stoprange)
    header["SetDataContent"] = setDataContent(s)
    header["SetEchoFilter"] = setEchoFilter(s)
    header["StorePermanently"] = storePermanently(s)
    header["ReadDeviceStatus"] = readDeviceStatus(s)
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
        flags["CONFIG"] = True


# Send data request message
def run(s):
    s.send(b'\x02sEN LMDscandata 1\x03\0')
    trash = s.recv(BUFFER)



def reboot(s):
    rebootvisual()
    s.send(b'\x02sMN mSCreboot\x03')


def receive(s):
    return s.recv(BUFFER)


def startup():
    loadingbar(1)
    s = createSocket()
    loadingbar(2)
    connect(s)
    loadingbar(3)
    header = loadconfig(s)
    loadingbar(4)
    failCheck(header)
    loadingbar(5)
    loadingbar(6)
    run(s)
    return s
