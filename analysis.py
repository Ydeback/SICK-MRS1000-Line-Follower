# Analysis of the preprocessed data for calculations of position

from __ANALYSIS__ import *

# Calculate the position and place it in an array.
# @return the offset length to the centre of the lidar, the index of the
# data point used, and the angle of the indexed data point
def position(filtered, layer, angle, pos, cableangle):
    index = np.where(filtered == np.amin(filtered))
    ind = index[0]
    ind = ind[0]
    rad = angle*np.pi/180
    x = np.sin(rad)
    y = np.multiply(x[ind], filtered[ind])
    z = rad[ind]
    cableangle[layer] = z
    pos[layer] = y
    return pos, ind, cableangle


# @return an array holding the length of the closest scan point for each
# layer
def lengthArray(filtered, layer, ind, length):
    z = filtered[ind]
    length[layer] = z
    return length


# Store the best position hit of the hit cable
# @return the reset pos array, the chosen position for the scan and the layer
# it corresponds to
def posLayerSafety(pos):
    hitlayer = 0
    for pos_after_check in pos:
        if pos_after_check == 99:
            hitlayer = hitlayer + 1
        else:
            break
   
   # Limit the number of hit layers for safety
    if hitlayer > 3:
        hitlayer = 3

    # If no hit was made a flag for 
    if pos_after_check == 99:
        flags["MISS"] += 1
    else:
        flags["MISS"] = 0
    
    # Reset the pos array for the next while iteration
    pos = np.double([0, 0, 0, 0])
    return pos, pos_after_check, hitlayer

