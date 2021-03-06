# Postprocessing of the data for preparation for LED compatible format

from __POSTPROCESS__ import *

# Method to convert the position of the target to a corresponding led in the
# led strip
# @return the positional led number to be lit
def convertPositionToLed(posaftercheck, length, cableangle, header):
    value = posaftercheck
    
    # Convert the left range into a 0-1 range (float)
    valuescaled = float(value - lidarmin) / float(lidarspan)
    
    # Convert the 0-1 range into a value in the right range.
    return round(ledstart + (valuescaled * ledrange))

