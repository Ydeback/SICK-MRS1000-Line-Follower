#
# Preprocessing of the input data
#

import collections
import numpy


# Convert measured data from binary
def fromBinary(data): 
    if b'+' in data or b'-' in data:
        return int(data)
    else:
        return int(data, 16)

# Identify the layers from each input
def layerCheck():
    layer = header['Layer']
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
    return header['StartingAngle']

# Returns the stop angle of the reading
def stopAngle():
    return header['StartingAngle']+header['AngularStepWidth']*header['NumberOfData']

# Parse the received data stream and sorting from the start and stop sign of
# ASCII
def datagram(received):

    STX = b'\x02'
    ETX = b'\x03'

    while True:
        datagram = b''

        for byte in received:
            if byte == STX:
                break

        for byte in received:
            if byte == ETX:
                break
            datagram += byte
        yield datagram

# Converts the measured data from millimeters to meters
def toMeter(milli):
    return milli/1000

# Assigns the data to an array variable
def toArray():
    return np.array(header['Data'])

# Decoding of the received data stream
def decodeDatagram(datagram):
    MRS1000 = collections.namedtuple("MRS1000_Datagram", ["TypeOfCommand", "Command", "VersionNumber", "DeviceNumber", "SerialNumber", "DeviceSatus1", "DeviceSatus2", "TelegramCounter", "ScanCounter", "TimeSinceStartup", "TimeOfTransmission", "InputStatus1", "InputStatus2", "OutputStatus1", "OutputStatus2", "ScanningFrequency", "MeasurementFrequency", "NumberOfEncoders", "NumberOf16bitChannels", "MeasuredDataContents", "ScalingFactor", "ScalingOffset", "StartingAngle", "AngularStepWidth", "NumberOfData", "Data"]) # "NumberOf8BitChannels", # "Position", # "Name", # "Comment", # "TimeInformation", # "EventInformation"])

    items = splitdata(datagram)

    header = {}
    header['TypeOfCommand'] = items[0].decode('ascii')
    if header['TypeOfCommand'] != 'sSN':
        return None
    header['Command'] = items[1].decode('ascii')
    if header['Command'] != 'LMDscandata':
        return None
    header['VersionNumber'] = fromBinary(items[2])
    header['DeviceNumber'] = fromBinary(items[3])
    header['SerialNumber'] = items[4].decode('ascii')
    header['DeviceStatus1'] = fromBinary(items[5])
    header['DeviceStatus2'] = fromBinary(items[6])
    if header['DeviceStatus1'] != 0 or header['DeviceStatus2'] != 0:
        return None
    header['TelegramCounter'] = fromBinary(items[7])
    header['TimeSinceStartup'] = fromBinary(items[9])
    header['TimeOfTransmission'] = fromBinary(items[10])
    header['Layer'] = item[15]
    header['StartingAngle'] = fromBinary(items[23])
    header['AngularStepWidth'] = fromBinary(items[24])
    header['NumberOfData'] = fromBinary(items[25])
    header['Data'] = [toMeter(fromBinary(x)) for x in items[26:26+header['NumberOfData']]]
    
    return header

# Main function of the preprocessing
def preprocess():
    # Receive and parse the received data
    datagram = next(datagram(received))
    
    # Assign values to the named tuole
    header = decodedatagram(datagram)
    
    # Create the array of angles for each data point 
    angle = angle()

    # Create an array of the measrued data in meter
    data = toArray()
