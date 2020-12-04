# Methodset for the interrupt methods used when the I/O of the Raspberry Pi4 is
# used

from __MAIN__ import flags
from __VISUALS__ import *
import RPi.GPIO as GPIO


# Method for when the dim button is pressed
def dimButton(channel):
    print("DIM")
    Col["AUTO"] = False
    Col["DIM"] += diminc
    if Col["DIM"] > 255:
        Col["DIM"] = 5


# Method for when the color for changing the led color to red is pressed
def redButton(channel):
    Col["RGB"] = 1
    print("red")

# Method for when the color for changing the led color to green is pressed
def greenButton(channel):
    Col["RGB"] = 2
    print("green")

# Method for when the color for changing the led color to blue is pressed
def blueButton(channel):
    Col["RGB"] = 3
    print("blue")

# Method for when the auto dim button is pressed
def autoButton(channel):
    Col["AUTO"] = True
    print(Col["AUTO"])

# Method for when the reboot button is pressed
def rebootButton(channel):
    flags["REBOOT"] = True
    print(flags["REBOOT"])

# Method for when the start led button is pressed
def startButton(channel):
    if Col["START"] == True:
        Col["START"] = False
    else:
        Col["START"] = True
    print(Col["START"])

# Attribute to represent the debounce time used on the buttons
bouncetime = 250

# Set the numbering mode on the GPIO interface
GPIO.setmode(GPIO.BCM)

# Initialize the start led button
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(6, GPIO.FALLING, callback = startButton, bouncetime = bouncetime)

# Initialize the color blue button
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(26, GPIO.FALLING, callback = blueButton, bouncetime = bouncetime)

# Initialize the color red button
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(16, GPIO.FALLING, callback = redButton, bouncetime = bouncetime)

# Initialize the color green button
#GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.add_event_detect(5, GPIO.FALLING, callback = greenButton, bouncetime = bouncetime)

# Initialize the dim button
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(23, GPIO.FALLING, callback = dimButton, bouncetime = bouncetime)

# Initialize the auto dim button
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(12, GPIO.FALLING, callback = autoButton, bouncetime = bouncetime)

# Initialize the reboot button
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(24, GPIO.FALLING, callback = rebootButton, bouncetime = bouncetime)

