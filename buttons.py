# Methodset for the interrupt methods used when the I/O of the Raspberry Pi4 is
# used

from __INIT__ import flags
from __VISUALS__ import *
import RPi.GPIO as GPIO


def dimButton(channel):
    Col["AUTO"] = False
    print("dim")
    Col["DIM"] += diminc
    if Col["DIM"] > 255:
        Col["DIM"] = 5

def redButton(channel):
    Col["RGB"] = 1

def greenButton(channel):
    Col["RGB"] = 2

def blueButton(channel):
    Col["RGB"] = 3
    print("blue")

def autoButton(channel):
    Col["AUTO"] = True
    print("auto")

def rebootButton(channel):
    flags["REBOOT"] = True

def startLED(channel):
    print("Start")
    if Col["START"] == True:
        Col["START"] = False
    else:
        Col["START"] = True

def autodim(channel):
    Col["LIGHT"] = lightSensor()

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(14, GPIO.RISING, callback = startLED, bouncetime = 300)

GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(15, GPIO.RISING, callback = blueButton, bouncetime = 300)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(18, GPIO.RISING, callback = dimButton, bouncetime = 300)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(23, GPIO.RISING, callback = autoButton, bouncetime = 300)

# GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.add_event_detect(25, GPIO.RISING, callback = lightSensor, bouncetime = 300)

#GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.add_event_detect(15, GPIO.RISING, callback = redButton, bouncetime = 300)

#GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.add_event_detect(18, GPIO.RISING, callback = greenButton, bouncetime = 300)

#GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.add_event_detect(8, GPIO.RISING, callback = rebootButton, bouncetime = 300)



