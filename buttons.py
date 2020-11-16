# Methodset for the interrupt methods used when the I/O of the Raspberry Pi4 is
# used

from __VISUALS__ import rebootflag
import RPi.GPIO as GPIO

def dimButton():
    Col["AUTO"] = False
    Col["DIM"] += diminc
    if Col["DIM"] > 255:
        Col["DIM"] = 0

def redButton(channel):
    Col["RGB"] = 1

def greenButton(channel):
    Col["RGB"] = 2

def blueButton(channel):
    Col["RGB"] = 3

def autoButton(channel):
    Col["AUTO"] = True

def rebootButton(channel):
    global rebootflag
    rebootflag = True
    print(rebootflag)

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(23, GPIO.RISING, callback = rebootButton, bouncetime = 300)
