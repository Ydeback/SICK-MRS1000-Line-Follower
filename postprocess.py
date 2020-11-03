# Postprocessing of the data for preparation for LED compatible format
def convertposition_to_led(i):
    value = i
    leftMin = -1.4
    leftMax = 1.4
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