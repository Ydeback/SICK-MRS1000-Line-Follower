# Method set for the preprocessing features of the program

from __PREPROCESS__ import *

# Convert measured data from binary
def fromBinary(data): 
    if b'+' in data or b'-' in data:
        return int(data)
    else:
        return int(data, 16)

# Identify the layers from each input
def layerCheck(layer):
    if layer == b'FE0C':
        return 0
    elif layer == b'FF06':
        return 1
    elif layer == b'0':
        return 2
    elif layer == b'FA':
        return 3

# Split the data into datapoints
def splitData(data): 
    return data.split(b' ')

# Create angular array from measured start and stop angle
def getAngle(header):
    return np.linspace(header["StartingAngle"], stopAngle(header), header["NumberOfData"])
    
# Returns the stop angle of the reading
def stopAngle(header):
    return  header["StartingAngle"]-header["AngularStepWidth"]*(header["NumberOfData"]-1)

# Converts the measured data from millimeters to meters
def toMeter(x):
    return x/1000

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

