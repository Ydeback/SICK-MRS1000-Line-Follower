# Postprocessing of the data for preparation for LED compatible format

from __POSTPROCESS__ import *

def convertPositionToLed(posaftercheck, length, cableangle, header):
    value = posaftercheck
    
    # Scaling based on the reading angle.
    # lidarmin = math.tan(math.radians(header["StartingAngle"]))*math.cos(cableangle)*length
    # lidarmax = math.tan(math.radians(header["StopAngle"]))*math.cos(cableangle)*length
    
    #####
    # lidarspan = lidarmax - lidarmin
    ####
    # Convert the left range into a 0-1 range (float)
    valuescaled = float(value - lidarmin) / float(lidarspan)
    # Convert the 0-1 range into a value in the right range.
    return round(ledstart + (valuescaled * ledrange))

