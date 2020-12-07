# Methodset for the interrupt methods used when the I/O of the Raspberry Pi4 is
# used

from __MAIN__ import flags
from __VISUALS__ import *
import RPi.GPIO as GPIO

# Method for when the dim up button is pressed
def dimUpButton(channel):
    Col["AUTO"] = False
    Col["DIM"] += diminc
    if Col["DIM"] > 255:
        Col["DIM"] = 255

# Method for when the color for changing the led color is pressed
def colorButton(channel):
    Col["RGB"] += 1
    if Col["RGB"] > 3:
        Col["RGB"] = 1

# Method for when the dim down button is pressed
def dimDownButton(channel):
    Col["AUTO"] = False
    Col["DIM"] -= diminc
    if Col["DIM"] < 5:
        Col["DIM"] = 5

# Method for when the auto dim button is pressed
def autoButton(channel):
    Col["AUTO"] = True

# Method for when the reboot button is pressed
def rebootButton(channel):
    flags["REBOOT"] = True

# Method for when the start led button is pressed
def startButton(channel):
    if Col["START"] == True:
        Col["START"] = False
        strip.clear_strip()
    else:
        Col["START"] = True

# Attribute to represent the debounce time used on the buttons
bouncetime = 500 

# Set the numbering mode on the GPIO interface
GPIO.setmode(GPIO.BCM)

# Initialize the start led button
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(6, GPIO.FALLING, callback = startButton, bouncetime = bouncetime)

# Initialize the auto dim button
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(12, GPIO.FALLING, callback = autoButton, bouncetime = bouncetime)

# Initialize the color red button
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(16, GPIO.FALLING, callback = colorButton, bouncetime = bouncetime)

# Initialize the dim button
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(23, GPIO.FALLING, callback = dimUpButton, bouncetime = int(bouncetime/2))

# Initialize the reboot button
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(24, GPIO.FALLING, callback = rebootButton, bouncetime = bouncetime)

# Initialize the color blue button
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(26, GPIO.FALLING, callback = dimDownButton, bouncetime = int( bouncetime/2))
