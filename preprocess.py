# Method set for the preprocessing features of the program

from __PREPROCESS__ import *

# Convert measured data from binary
# @return the encoded data
def fromBinary(data): 
    if b'+' in data or b'-' in data:
        return int(data)
    else:
        return int(data, 16)


# Identify the layers from each input
# @return the layer of the scanned data
def layerCheck(layer):
    if layer == b'FE0C':
        return 0
    elif layer == b'FF06':
        return 1
    elif layer == b'0':
        return 2
    elif layer == b'FA':
        return 3


# @return the split data
def splitData(data): 
    return data.split(b' ')


# @return an  angular array from measured start and stop angle
def getAngle(header):
    return np.linspace(header["StartingAngle"], stopAngle(header), header["NumberOfData"])


# @return the stop angle of the reading
def stopAngle(header):
    return  header["StartingAngle"]-header["AngularStepWidth"]*(header["NumberOfData"]-1)


# @return the measured data from millimeters to meters
def toMeter(x):
    return x/1000


# Decoding of the received data stream
def decodeDatagram(data):
    # Split the incoming data string
    datapoints = splitData(data)

    header["NumberOfData"] = fromBinary(datapoints[25])
    header["Data"] = [toMeter(fromBinary(x)) for x in datapoints[26:26+header["NumberOfData"]]]
    header["StartingAngle"] = 90-fromBinary(datapoints[23])/10000
    header["AngularStepWidth"] = fromBinary(datapoints[24])/10000
    header["StopAngle"] = header["StartingAngle"]-header["AngularStepWidth"]*(header["NumberOfData"]-1)
    header["Layer"] = datapoints[15]
    if remang == b'1':
        header["RSSI"] = [fromBinary(x) for x in datapoints[26+header["NumberOfData"]+6:26+header["NumberOfData"]*2+6]]
    # header["AINF"] = datapoints[]
    return header

