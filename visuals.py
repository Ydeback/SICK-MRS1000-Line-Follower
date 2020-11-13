# Visualisation to the LEDs
from apa102_pi.driver import apa102
import RPi.GPIO as GPIO
from collections import namedtuple as nt
import time
import RPi.GPIO as GPIO
import RPi.GPIO as GPIO_DIM
import time

from startup import rebootFLAG

BUFFER = 2064
strip = apa102.APA102(num_led=50, order='rgb')

NamedTuple = nt("Colors", ["RGB", "dim", "auto"])
Col = {}
Col["RGB"] = 1
Col["dim"] = 55
Col["auto"] = False

def colorSwitcher(i, dim):
    switcher = {
        1: "0x%02x%02x%02x" % (dim, 0, 0),
        2: "0x%02x%02x%02x" % (0, dim, 0),
        3: "0x%02x%02x%02x" % (0, 0, dim),
        # 4: "0x%02x%02x%02x" % (0, dim, dim),
        # 5: "0x%02x%02x%02x" % (dim, 0, dim),
        # 6: "0x%02x%02x%02x" % (dim, dim, 0),
    }
    return int(switcher.get(i), 16)

def dimbutton(channel):
    Col["auto"] = False
    Col["dim"] += 40
    if Col["dim"] > 255:
        Col["dim"] = 0

def redButton(channel):
    Col["RGB"] = 1

def greenButton(channel):
    Col["RGB"] = 2

def blueButton(channel):
    Col["RGB"] = 3

def autoButton(channel):
    Col["auto"] = True

def autoLight():
    if Col["auto"] == True:
        leftMin_light = 600
        leftMax_light = 0
        rightMin_light = 0
        rightMax_light = 255

        # Figure out how 'wide' each range is
        leftSpan_light = leftMax_light - leftMin_light
        rightSpan_light = rightMax_light - rightMin_light

        light_value = light_sensor()

        if light_value > leftMin_light - 3:
            light_value = leftMin_light - 3

        # Convert the left range into a 0-1 range (float)
        LightvalueScaled = (light_value - leftMin_light) / leftSpan_light

        # Convert the 0-1 range into a value in the right range.
        light = round(rightMin_light + (LightvalueScaled * rightSpan_light))

        Col["dim"] = light
        if Col["dim"] > 255:
            Col["dim"] = 0

# Reboot the device
def rebootButton(channel):
    rebootFLAG[0] = True


GPIO.setmode(GPIO.BCM)
#GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# redButton
#GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# greenButton
#GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# blueButton
#GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.add_event_detect(23, GPIO.RISING, callback=dimbutton, bouncetime=300)
#GPIO.add_event_detect(11, GPIO.RISING, callback=redButton, bouncetime=300)
#GPIO.add_event_detect(12, GPIO.RISING, callback=greenButton, bouncetime=300)
#GPIO.add_event_detect(13, GPIO.RISING, callback=blueButton, bouncetime=300)
GPIO.add_event_detect(14, GPIO.RISING, callback=rebootButton, bouncetime=300)


#GPIO.add_event_detect(25, GPIO.RISING, callback=rebootbutton, bouncetime=300)

def visual(ledValue):
    strip.clear_strip()
    print(ledValue)
    color = colorSwitcher(Col["RGB"], Col["dim"])  # Col["light"]
    strip.set_pixel_rgb(24, color)
    strip.set_pixel_rgb(26, color)
    strip.set_pixel_rgb(49, 0x220000)
    strip.set_pixel_rgb(0, 0x220000)
    strip.set_pixel_rgb(ledValue, color)
    strip.show()


def light_sensor():
    resistorPin = 4

    GPIO.setup(resistorPin, GPIO.OUT)
    GPIO.output(resistorPin, GPIO.LOW)
    time.sleep(0.0001)

    GPIO.setup(resistorPin, GPIO.IN)
    currentTime = time.time()
    diff = 0

    while (GPIO.input(resistorPin) == GPIO.LOW):
        diff = time.time() - currentTime

    return (round(diff * 1000000))

    # time.sleep(10)
