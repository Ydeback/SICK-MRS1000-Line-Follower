#
# Preprocessing of the input data
#

from collections import namedtuple as nt 
import numpy as np


# Convert measured data from binary
def fromBinary(data): 
    if b'+' in data or b'-' in data:
        return int(data)
    else:
        return int(data, 16)

# Identify the layers from each input
def layerCheck():
    layer = header["Layer"]
    if layer == b'FE0C':
        print("Layer: 4")
    elif layer == b'FF06':
        print("Layer: 3")
    elif layer == b'0':
        print("Layer: 2")
    elif layer == b'FA':
        print("Layer: 1")

# Split the data into datapoints
def splitData(data): 
    return data.split(b' ')

# Create angular array from measured start and stop angle
def angle(): 
    return np.linspace(startAngle(), stopAngle(), dataPoints())    
    
# Returns the starting angle of the reading
def startAngle():
    return header["StartingAngle"]

# Returns the stop angle of the reading
def stopAngle():
    return  header["StartingAngle"]+header["AngularStepWidth"]*header["NumberOfData"]

# Converts the measured data from millimeters to meters
def toMeter(data):
    return data/1000

# Decoding of the received data stream
def decodeDatagram(data):
    NamedTuple = nt("MRS1000",["TypeOfCommand", "Command", "VersionNumber", "DeviceNumber", "SerialNumber", "DeviceSatus1", "DeviceSatus2", "TelegramCounter", "ScanCounter", "TimeSinceStartup", "TimeOfTransmission", "InputStatus1", "InputStatus2", "OutputStatus1", "OutputStatus2", "ScanningFrequency", "MeasurementFrequency", "NumberOfEncoders", "NumberOf16bitChannels", "MeasuredDataContents", "ScalingFactor", "ScalingOffset", "StartingAngle", "AngularStepWidth", "NumberOfData", "Data"]) 

    datapoints = splitData(b' ')

    header = {}
    header["NumberOfData"] = fromBinary(datapoints[25])
    header["Data"] = [toMeter(fromBinary(data)) for data in datapoints[26:26+header["NumberOfData"]]]

    return header

