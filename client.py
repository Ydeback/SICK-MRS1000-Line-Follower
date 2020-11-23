# Client configuration of MRS1000c LiDAR

from __CLIENT__ import *
from __INIT__ import *
from __VISUALS__ import strip
from visuals import *

# Construction of a socket object (TCP)
# @return the socket object
def createSocket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Connect to the server side (LiDAR)
# @return bool, True if the connection failed, False if the connection was
# successful
def connect(s):
    s.settimeout(timeout)
    try:
        s.connect(ADDRESS)
    except socket.error:
        connectFailVisual()
        return True
    return False


# Login as Authorized client
# @return the answer received from the LiDAR
def login(s):
    try:
        s.send(b'\x02sMN SetAccessMode 03 F4724744\x03')
    except socket.error as err:
        pass
    return s.recv(BUFFER)


# Method for converting decimal values to hexadecimal values
def fromDecToHex(x):
    return bytes(hex(x).split('x')[-1].upper(), encoding='ascii')


# Set output data range
# @return the answer from the LiDAR
def setDataRange(s, startrange, stoprange):
    s.send(b'\x02sWN LMPoutputRange 1 9C4 ' + stop + b' ' + start + b'\x03')
    return s.recv(BUFFER)


# Configure the data output content
# @return the answer received from the LiDAR
def setDataContent(s):
    s.send(b'\x02sWN LMDscandatacfg 00 00 ' + remang  + b' ' + remres + b' 0 0 0 ' + position + b' ' + devicename + b' ' + comment + b' ' + timeinfo + b' 01\x03')
    return s.recv(BUFFER)


# Set the echo filter
# @return the answer received from the LiDAR
def setEchoFilter(s):
    s.send(b'\x02sWN FREchoFilter ' + echo + b'\x03')
    return s.recv(BUFFER)


#Set the partticle filter
# @return the answer received from the LiDAR
def setParticleFilter(s):
    s.send(b'\x02sWN LFPparticle ' + particle + b' ' + fromDecToHex(particlesize * 1000) + b'\x03')
    return s.recv(BUFFER)


#Set the mean filter
# @return the answer received from the LiDAR
def setMeanFilter(s):
    s.send(b'\x02sWN LFPmeanfilter ' + mean + b' ' + fromDecToHex(nummean) + b' 0\x03')
    return s.recv(BUFFER)


# Set the median filter
# @return the answer received from the LiDAR
def setMedianFilter(s):
    s.send(b'\x02sWN LFPmedianfilter ' + median + b' 3\x03')
    return s.recv(BUFFER)


# Read device status (Ready, logged-in, error)
# @return the answer received from the LiDAR
def readDeviceStatus(s):
    s.send(b'\x02sRN SCdevicestate\x03')
    return s.recv(BUFFER)


# Store configuration permanently
# @return the answer received from the LiDAR
def storePermanently(s):
    s.send(b'\x02sMN mEEwriteall\x03')
    return s.recv(BUFFER)


# Unit and encoding changes for the parameter variables
stop = fromDecToHex((90 - startrange) * 10000)
start = fromDecToHex((90 + stoprange) * 10000)

# Loading the config of the MRS1000c LiDAR
# @return the tuple containing the answers from the LiDAR
def loadconfig(s):
    # Fill the tuple with the answers from the LiDAR
    config["Login"] = login(s)
    config["SetDataRange"] = setDataRange(s, startrange, stoprange)
    config["SetDataContent"] = setDataContent(s)
    config["SetEchoFilter"] = setEchoFilter(s)
    config["SetParticleFilter"] = setParticleFilter(s)
    config["SetMeanFilter"] = setMeanFilter(s)
    config["SetMedianFilter"] = setMedianFilter(s)
    config["StorePermanently"] = storePermanently(s)
    config["ReadDeviceStatus"] = readDeviceStatus(s)
    
    return config


# Check if all the config settings has been set successfully
# @return the state of the success of the configuration procedure
def failCheckFunc(header):
    if header["Login"] != b'\x02sAN SetAccessMode 1\x03':
        return True
    elif header["SetDataRange"] != b'\x02sWA LMPoutputRange\x03':
        return True
    elif header["SetDataContent"] != b'\x02sWA LMDscandatacfg\x03':
        return True
    elif header["ReadDeviceStatus"] == b'\x02sRA SCdevicestate 2\x03':
        return True
    elif header["SetEchoFilter"] != b'\x02sWA FREchoFilter\x03':
        return True
    elif header["SetParticleFilter"] != b'\x02sWA LFPparticle\x03':
        return True
    elif header["SetMeanFilter"] != b'\x02sWA LFPmeanfilter\x03':
        return True
    elif header["SetMedianFilter"] != b'\x02sWA LFPmedianfilter\x03':
        return True
    elif header["StorePermanently"] == b'\x02sAN mEEwriteall 0\x03':
         return True
    else:
        return False


# Function to handle the fail of configuration of the LiDAR
# @return Bool, True if the config failed, False if the config was succesful
def failCheck(header):
    if failCheckFunc(header):
        # Runs the visualisation representating the fail of
        # configuration
        configFailVisual()
        return True
    return False


# Send data request message
# @return the answer received from the LiDAR
def run(s):
    s.send(b'\x02sEN LMDscandata 1\x03\0')
    trash = s.recv(BUFFER)


# Method for when the reboot button has been pressed
def reboot(s):
    # Visualisation method for when the reboot is initialized
    rebootVisual()

    # Reboot command sent to the LiDAR
    try:
        s.send(b'\x02sMN mSCreboot\x03')
    except socket.error:
        pass
   ### To be activated in final version ###
   # os.system("sudo shutdown -r now")


# Method for receiving data from the LiDAR
# @return the data received from the LiDAR
def receive(s):
    return s.recv(BUFFER)


# Method for the startup procedure of the LiDAR
# @return the socket object
def startup():
    loadingbar(1)
    s = createSocket()
    loadingbar(2)
    if connect(s):
        return s
    loadingbar(3)
    header = loadconfig(s)
    loadingbar(4)
    if failCheck(header):
        return s
    loadingbar(5)
    loadingbar(6)
    run(s)
    strip.clear_strip()
    return s
