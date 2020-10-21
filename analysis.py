# Analysis of the preprocessed data for calculations of position
import numpy as np

def position(data,layer, angle):

    # Identify both cabels
    index1 = np.where(data == np.amin(data))

    # value of the accepted distances
    #print('Dist1:', arr[index1[0]])

    # LiDAR measurement
    x = np.sin(angle)
    y = np.multiply(x[index1[0]], data[index1[0]])
    pos = y[0]
    return pos


# Convert the data to meters
def distance(data): 
    pass

# Measure the truck offset from the cables
def offset(): 
    pass

