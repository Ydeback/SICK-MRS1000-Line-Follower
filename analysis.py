# Analysis of the preprocessed data for calculations of position
import numpy as np
import time

# Calculate the position and place it in an array.
def position(data, layer, angle, pos, cabel_angle):

    # Identify one cabel
    index1 = np.where(data == np.amin(data))

    # value of the accepted distances
    #print('Dist1:', arr[index1[0]])

    # LiDAR measurement
    rad = angle*np.pi/180
    x = np.sin(rad)
    y = np.multiply(x[index1[0]], data[index1[0]])
    z = rad[index1[0]]
    cabel_angle[layer] = z[0]
    pos[layer] = y[0]
    return pos, index1, cabel_angle

def lengtharray(data, layer, index1, length):
    z = data[index1[0]]
    length[layer] = z[0]
    return length


# Print the best position
def pos_layersafety(pos):
    i = 0
    for pos_after_check in pos:
        if pos_after_check == 99:
            i = i + 1
            continue
        else:
            break
    if pos_after_check == 99:
        print('Error: No hit!')
    pos = np.double([0, 0, 0, 0])
    return pos, pos_after_check, i

def output_time(t):
    # Time for output
    elapsed = time.time() - t
    print('DeltaT:',elapsed, 's')
    t = time.time()
    return t