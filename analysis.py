# Analysis of the preprocessed data for calculations of position

from __ANALYSIS__ import *

# Calculate the position and place it in an array.
def position(filtered, layer, angle, pos, cableangle):
    index = np.where(filtered == np.amin(filtered))
    rad = angle*np.pi/180
    x = np.sin(rad)
    y = np.multiply(x[index[0]], filtered[index[0]])
    z = rad[index[0]]
    cableangle[layer] = z[0]
    pos[layer] = y[0]
    return pos, index, cableangle

def lengthArray(filtered, layer, index, length):
    z = filtered[index[0]]
    length[layer] = z[0]
    return length

# Store the best position hit of the hit cable
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

