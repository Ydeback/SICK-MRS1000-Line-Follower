# Visualisation to the LEDs

from __VISUALS__ import *
from buttons import *


# Method for the color switcher for the position led
# @return the preset color with the given brightness value
def colorSwitcher(i, dim):
    switcher = {
        1: "0x%02x%02x%02x" % (dim, 0, 0),
        2: "0x%02x%02x%02x" % (0, dim, 0),
        3: "0x%02x%02x%02x" % (0, 0, dim)
    }
    return int(switcher.get(i), 16)



# Method for the color switch for the fixed marker leds
# @return the preset color with the given brightness value
def colorSwitcherSides(i, dim):
    switcher = {
        2: "0x%02x%02x%02x" % (dim, 0, 0),
        1: "0x%02x%02x%02x" % (0, dim, 0),
        3: "0x%02x%02x%02x" % (dim, dim, 0)
    }
    return int(switcher.get(i), 16)



# Method for the visualisation of the led strip
def visual(x):
    # Clear the strip
    strip.clear_strip()
    if Col["START"]:
        autoLight()
        # @return the color with the current dim strength of the positional led
        color = colorSwitcher(Col["RGB"], Col["DIM"])
        
        # @return the color with the current dim strength of the fixed marker
        # leds
        colorSides = colorSwitcherSides(Col["RGB"], Col["DIM"])
        # Setting the specification for the specified leds
        strip.set_pixel_rgb(44, colorSides)
        strip.set_pixel_rgb(48, colorSides)
        strip.set_pixel_rgb(92, colorSides)
        strip.set_pixel_rgb(0, colorSides)
        strip.set_pixel_rgb(x, color)

        # Display the led with current settings
        strip.show()

# visualisation for when the configuration of the LiDAR has failed
def configFailVisual():
    strip.clear_strip()
    for x in range(nleds):
        if (x%10==0):
            strip.set_pixel_rgb(x, colorSwitcher(1, Col["DIM"]))
    strip.show()
    time.sleep(3)
    flags["REBOOT"] = True


# visualisation for when the connection to the LiDAR has failed
def connectFailVisual():
    strip.clear_strip()
    for x in range(nleds):
        if (x%10==0):
            strip.set_pixel_rgb(x, colorSwitcher(3, Col["DIM"]))
    strip.show()
    time.sleep(3)
    flags["REBOOT"] = True


# Visualisation for when the target has been missed to many times in a row
def missVisual():
    if flags["MISS"] > missthreshold:
        strip.clear_strip()
        for x in range(nleds):
            strip.set_pixel_rgb(x, colorSwither(3, Col["DIM"]))


# Visualisation for when the system is set to reboot mode
def rebootVisual():
    strip.clear_strip()
    for x in range(nleds):
        strip.set_pixel_rgb(nleds + 1 - x, colorSwitcher(1, Col["DIM"]))
        strip.show()
        time.sleep(0.01)


# Method for the intervals of the auto dimming
# @return the brightness of the leds
def interval(x):
    if x <=80:
        return 5
    elif x > 80 and x <= 150:
        return 80
    elif x > 150 and x <= 230:
        return 150
    else:
        return 230


# Method for setting the brightness from the input of the photoresistor sensor
def autoLight():
    if Col["AUTO"]:

        # @return sensoroutput
        sensorvalue = lightSensor()
        
        # If the sensorvalue exceeds the set max sensor value, limit the value
        if sensorvalue > sensormax - 3:
            sensorvalue = sensormax - 3

        # Convert the sensorspan into a 0-1 range (float)
        sensorvaluescaled = (sensorvalue - sensormax) / sensorspan

        # Convert the 0-1 range into a value in the ledspan.
        light = interval(round(ledmin + (sensorvaluescaled * ledspan)))
        
        # Set the dim value
        Col["DIM"] = light
        if Col["DIM"] > 255:
            Col["DIM"] = 255


# Method to receive the brightness input from the photoresistor sensor
# @return the brightness level appreciated from the surrounding environment
def lightSensor():
    # Set the I/O for the pin to output
    GPIO.setup(25, GPIO.OUT)
    # Set the output mode to LOW
    GPIO.output(25, GPIO.LOW)
    # Set pin mode to input
    GPIO.setup(25, GPIO.IN)
    # Get the current time
    currentTime = time.time()
    # Reset the time difference attribute
    diff = 0
    # While the input is LOW, get the time difference
    while (GPIO.input(25) == GPIO.LOW):
        diff = time.time() - currentTime
    return (round(diff * 100000))


# Method for the visualisation for when the system is in startup mode
def loadingbar(commandsdone):
    autoLight()
    if commandsdone < 6:
        for leds in range(commandsdone*19):
            strip.set_pixel_rgb(leds, colorSwitcher(2, Col["DIM"]))
            strip.show()
            time.sleep(0.005)
    # else:
        # time.sleep(0.5)
        # strip.clear_strip()
        # time.sleep(0.5)
        # for leds in range(93):
            # strip.set_pixel_rgb(leds, colorSwitcher(2, Col["DIM"]))
            # strip.show()
            # time.sleep(0.01)
        # time.sleep(1)
