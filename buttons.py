# Methodset for the interrupt methods used when the I/O of the Raspberry Pi4 is
# used

from __MAIN__ import flags
from __VISUALS__ import *
import RPi.GPIO as GPIO


# Method for when the dim button is pressed
def dimButton(channel):
    Col["AUTO"] = False
    Col["DIM"] += diminc
    if Col["DIM"] > 255:
        Col["DIM"] = 5


# Method for when the color for changing the led color to red is pressed
def redButton(channel):
    Col["RGB"] = 1


# Method for when the color for changing the led color to green is pressed
def greenButton(channel):
    Col["RGB"] = 2
    print("green")


# Method for when the color for changing the led color to blue is pressed
def blueButton(channel):
    Col["RGB"] = 3


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
    else:
        Col["START"] = True


# Attribute to represent the debounce time used on the buttons
bouncetime = 350

# Set the numbering mode on the GPIO interface
GPIO.setmode(GPIO.BCM)

# Initialize the start led button
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(18, GPIO.FALLING, callback = startButton, bouncetime = bouncetime)

# Initialize the color blue button
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(26, GPIO.FALLING, callback = blueButton, bouncetime = bouncetime)

# Initialize the color red button
GPIO.setup(16 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(16, GPIO.FALLING, callback = redButton, bouncetime = bouncetime)

# Initialize the color green button
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(3, GPIO.FALLING, callback = greenButton, bouncetime = bouncetime)

# Initialize the dim button
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(15, GPIO.FALLING, callback = dimButton, bouncetime = bouncetime)

# Initialize the auto dim button
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(2, GPIO.FALLING, callback = autoButton, bouncetime = bouncetime)

# Initialize the reboot button
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(24, GPIO.FALLING, callback = rebootButton, bouncetime = 300)



