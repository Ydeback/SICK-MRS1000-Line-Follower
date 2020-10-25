# Analysis of the preprocessed data for calculations of position
import numpy as np
import time

# Calculate the position and place it in an array.
def position(data,layer, angle,pos):

    # Identify one cabel
    index1 = np.where(data == np.amin(data))

    # value of the accepted distances
    #print('Dist1:', arr[index1[0]])

    # LiDAR measurement
    x = np.sin(angle*np.pi/180)
    y = np.multiply(x[index1[0]], data[index1[0]])
    pos[layer] = y[0]
    return pos



# Print the best position
def pos_layersafety(pos):
    for i in pos:
        if i == 99:
            continue
        else:
            break
    if i == 99:
        print('Error: No hit!')
    pos = np.double([0, 0, 0, 0])
    return pos, i

def output_time(t):
    # Time for output
    elapsed = time.time() - t
    print('DeltaT:',elapsed, 's')
    t = time.time()
    return t