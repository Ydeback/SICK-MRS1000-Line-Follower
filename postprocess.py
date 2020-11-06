# Postprocessing of the data for preparation for LED compatible format
import math

def convertposition_to_led(pos_after_check, length, angle_cabel, header):
    value = pos_after_check
    #leftMin and leftMax is constant for the pantograf
    leftMin = math.tan(math.radians(header["StartingAngle"]))*math.cos(angle_cabel)*length
    leftMax = math.tan(math.radians(header["StopAngle"]))*math.cos(angle_cabel)*length
    rightMin = 0
    rightMax = 50
    #translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    led = rightMin + (valueScaled * rightSpan)

    led = round(led)
    return led