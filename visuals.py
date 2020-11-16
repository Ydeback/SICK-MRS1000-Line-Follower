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

def visual(x):
    # Clear the strip
    strip.clear_strip()
    # @return the color with the current dim strength of the positional led
    color = colorSwitcher(Col["RGB"], Col["DIM"])  # Col["light"]
    strip.set_pixel_rgb(44, color)
    strip.set_pixel_rgb(46, color)
    strip.set_pixel_rgb(89, 0x220000)
    strip.set_pixel_rgb(0, 0x220000)
    strip.set_pixel_rgb(x, color)
    # Display the led with current settings
    strip.show()


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
        light = round(ledmin + (sensorvaluescaled * ledspan))

        Col["DIM"] = light
        if Col["DIM"] > 255:
            Col["DIM"] = 255


###########
# redo as interrupt
###########
def lightSensor():
    # Set the I/O for the pin to output
    GPIO.setup(resistorPin, GPIO.OUT)
    # Set the output mode to LOW
    GPIO.output(resistorPin, GPIO.LOW)
    # Set pin mode to input
    GPIO.setup(resistorPin, GPIO.IN)
    # Get the current time
    currentTime = time.time()
    # Reset the time difference attribute
    diff = 0

    # While the input is LOW, get the time difference
    while (GPIO.input(resistorPin) == GPIO.LOW):
        diff = time.time() - currentTime

    return (round(diff * 1000000))
