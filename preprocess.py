#
# Preprocessing of the input data
#

import collections
import numpy as np


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

# Converts the measured data from millimeters to meters
def toMeter(milli):
    return milli/1000

# Assigns the data to an array variable
def toArray():
    return np.array(header['Data'])

# Decoding of the received data stream
def decodeDatagram():
    pass

# Main function of the preprocessing
def preprocess(received):
    print(received)

    # Assign values to the named tuple
    # header = decodeDatagram()
    
    # Create the array of angles for each data point 
    # angleArray = angle()

    # Create an array of the measrued data in meter
    # dataArray = toArray()
    
