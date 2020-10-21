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
def layerCheck(header):

    if header["Layer"] == b'FE0C':
        print("Layer: 4")
        return 0
    elif header["Layer"] == b'FF06':
        print("Layer: 3")
        return 1
    elif header["Layer"] == b'0':
        print("Layer: 2")
        return 2
    elif header["Layer"] == b'FA':
        print("Layer: 1")
        return 3



# Split the data into datapoints
def splitData(data): 
    return data.split(b' ')

# Create angular array from measured start and stop angle
def getAngle(header):
    return np.linspace(startAngle(header), stopAngle(header), header["NumberOfData"])
    
# Returns the starting angle of the reading
def startAngle(header):
    return header["StartingAngle"]

# Returns the stop angle of the reading
def stopAngle(header):
    return  header["StartingAngle"]-header["AngularStepWidth"]*(header["NumberOfData"]-1)

# Converts the measured data from millimeters to meters
def toMeter(data):
    return data/1000

# Decoding of the received data stream
def decodeDatagram(data):
    NamedTuple = nt("MRS1000",["TypeOfCommand", "Command", "VersionNumber", "DeviceNumber", "SerialNumber", "DeviceSatus1", "DeviceSatus2", "TelegramCounter", "ScanCounter", "TimeSinceStartup", "TimeOfTransmission", "InputStatus1", "InputStatus2", "OutputStatus1", "OutputStatus2", "ScanningFrequency", "MeasurementFrequency", "NumberOfEncoders", "NumberOf16bitChannels", "MeasuredDataContents", "ScalingFactor", "ScalingOffset", "StartingAngle", "AngularStepWidth", "NumberOfData", "Data"]) 

    datapoints = splitData(data)

    header = {}
    header["NumberOfData"] = fromBinary(datapoints[25])
    header["Data"] = [toMeter(fromBinary(x)) for x in datapoints[26:26+header["NumberOfData"]]]
    header["StartingAngle"] = 90-fromBinary(datapoints[23])/10000
    header["AngularStepWidth"] = fromBinary(datapoints[24])/10000
    header["StopAngle"] = header["StartingAngle"]-header["AngularStepWidth"]*(header["NumberOfData"]-1)
    header["Layer"] = datapoints[15]
    return header

