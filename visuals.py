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
    # Use the variable holding the last position led value
    global last_x
    # Clear the last led point
    strip.set_pixel_rgb(last_x, 0x000000)
    # If the start button is pressed, start the visualisation
    if Col["START"]:
        # Run the automatic dim function
        autoLight()
        # Check what color is currently preset for the position led
        color = colorSwitcher(Col["RGB"], Col["DIM"])
        # Check what color is currently preset for the fixed leds
        colorSides = colorSwitcherSides(Col["RGB"], Col["DIM"])
        # Assign the color settings for the fixed leds
        strip.set_pixel_rgb(44, colorSides)
        strip.set_pixel_rgb(48, colorSides)
        strip.set_pixel_rgb(0, colorSides)
        strip.set_pixel_rgb(1, colorSides)
        strip.set_pixel_rgb(2, colorSides)
        strip.set_pixel_rgb(90, colorSides)
        strip.set_pixel_rgb(91, colorSides)
        strip.set_pixel_rgb(92, colorSides)
        # Assign the color settings for the position led
        strip.set_pixel_rgb(x, color)
        # Apply the settings and light up the led strip
        strip.show()
    else:
        # If the start button is pressed when the leds is shown, clear the led
        # strip
        strip.clear_strip()
    # Set the current position led value as the previous position for the
    # next run
    last_x = x


# visualisation for when the configuration of the LiDAR has failed
def configFailVisual():
    strip.clear_strip()
    for x in range(nleds):
        if (x%10==0):
            strip.set_pixel_rgb(x, colorSwitcher(3, Col["DIM"]))
    strip.show()
    time.sleep(3)
    flags["REBOOT"] = True


# visualisation for when the connection to the LiDAR has failed
def connectFailVisual():
    strip.clear_strip()
    for x in range(nleds):
        if (x%10==0):
            strip.set_pixel_rgb(x, colorSwitcher(1, Col["DIM"]))
    strip.show()
    time.sleep(3)
    flags["REBOOT"] = True


# Visualisation for when the system is set to reboot mode
def rebootVisual():
    strip.clear_strip()
    for x in range(2):
        for x in range(nleds):
            strip.set_pixel_rgb(nleds + 1 - x, colorSwitcher(1, Col["DIM"]))
            strip.show()
            time.sleep(0.01)
    strip.clear_strip()

# Method for the intervals of the auto dimming
# @return the brightness of the leds
def interval(x):
    if x <= 55:
        return 5
    elif x > 55 and x <= 105:
        return 55
    elif x > 105 and x <= 155:
        return 105
    else:
        return 155


# Method for setting the brightness from the input of the photoresistor sensor
def autoLight():
    # If the auto button has been pressed
    if Col["AUTO"]:
        
        # Get the light sensor brightness value
        sensorvalue = lightSensor()
        # Cap the value
        if sensorvalue > sensormax:
            sensorvalue = sensormax
        
        # Scale the brightness value to match the led strip brightness cap
        sensorvaluescaled = (sensorvalue - sensormax) / sensorspan
        # Get a brightness value to the leds capped from specifies intervals
        light = interval(round(ledmin + (sensorvaluescaled * ledspan)))
        # Assign the brightness value to the tuple index holding the
        # brightness value
        Col["DIM"] = light
        # Cap the brightness value
        if Col["DIM"] > 255:
            Col["DIM"] = 255


# Method to receive the brightness input from the photoresistor sensor
# @return the brightness level appreciated from the surrounding environment
def lightSensor():
    # Set the I/O for the pin to output
    GPIO.setup(27, GPIO.OUT)
    # Set the output mode to LOW
    GPIO.output(27, GPIO.LOW)
    # Set pin mode to input
    GPIO.setup(27, GPIO.IN)
    # Get the current time
    currentTime = time.time()

    difference = 0
    # A for loop for getting the mean of the photoresistor
    for x in range(50):
        # Reset the time difference attribute
        diff = 0.0
        # While the input is LOW, get the time difference
        while (GPIO.input(27) == GPIO.LOW):
            diff = time.time() - currentTime
        difference = difference + (round(diff * 100000))
    return difference/50


# Method for the visualisation for when the system is in startup mode
def loadingbar(commandsdone):
    autoLight()
    if commandsdone < 6:
        for leds in range(commandsdone*19):
            strip.set_pixel_rgb(leds, colorSwitcher(2, Col["DIM"]))
            strip.show()
            time.sleep(0.005)
