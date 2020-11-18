# Visualisation to the LEDs

from __VISUALS__ import *
from buttons import *


def colorSwitcher(i, dim):
    switcher = {
        1: "0x%02x%02x%02x" % (dim, 0, 0),
        2: "0x%02x%02x%02x" % (0, dim, 0),
        3: "0x%02x%02x%02x" % (0, 0, dim)
    }
    return int(switcher.get(i), 16)

def colorSwitcherSides(i, dim):
    switcher = {
        2: "0x%02x%02x%02x" % (dim, 0, 0),
        1: "0x%02x%02x%02x" % (0, dim, 0),
        3: "0x%02x%02x%02x" % (dim, dim, 0)
    }
    return int(switcher.get(i), 16)

def visual(x):
    # Clear the strip
    strip.clear_strip()
    if Col["START"] == True:
        # @return the color with the current dim strength of the positional led
        autoLight()
        color = colorSwitcher(Col["RGB"], Col["DIM"])
        colorSides = colorSwitcherSides(Col["RGB"], Col["DIM"])
        strip.set_pixel_rgb(44, colorSides)
        strip.set_pixel_rgb(48, colorSides)
        strip.set_pixel_rgb(92, colorSides)
        strip.set_pixel_rgb(0, colorSides)
        strip.set_pixel_rgb(x, color)
        # Display the led with current settings
        strip.show()


def rebootvisual():
    strip.clear_strip()

def interval(x):
    if x <=80:
        return 5
    elif x > 80 and x <= 150:
        return 80
    elif x > 150 and x <= 230:
        return 150
    else:
        return 230

def autoLight():
    if Col["AUTO"]:
        # @return sensoroutput
        sensorvalue = lightSensor()
        # sensorvalue = Col["LIGHT"]
        # If the sensorvalue exceeds the set max sensor value, limit the value
        if sensorvalue > sensormax - 3:
            sensorvalue = sensormax - 3

        # Convert the sensorspan into a 0-1 range (float)
        sensorvaluescaled = (sensorvalue - sensormax) / sensorspan

        # Convert the 0-1 range into a value in the ledspan.
        light = interval(round(ledmin + (sensorvaluescaled * ledspan)))
        
        Col["DIM"] = light
        if Col["DIM"] > 255:
            Col["DIM"] = 255


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


def loadingbar(commandsdone):
    # Must be static values for color and dim here
    color = colorSwitcher(Col["RGB"], Col["DIM"])
    if commandsdone < 6:
        for leds in range(commandsdone*19):
            strip.set_pixel_rgb(leds, 0x00FF00, 30)
            strip.show()
    else:
        strip.clear_strip()
        time.sleep(0.5)
        for leds in range(93):
            strip.set_pixel_rgb(leds, 0x00FF00, 30)
            strip.show()
            time.sleep(0.01)
        time.sleep(1)
