# Visualisation to the LEDs
from apa102_pi.driver import apa102
import RPi.GPIO as GPIO
from collections import namedtuple as nt
import time
strip = apa102.APA102(num_led=50, order='rgb')

NamedTuple = nt("Colors",["RGB","dim"])
Col = {}
Col["RGB"] = 1
Col["dim"] = 55

def colorSwitcher(i,dim):
    switcher = {
        1: "0x%02x%02x%02x" % (dim, 0, 0),
        2: "0x%02x%02x%02x" % (0, dim, 0),
        3: "0x%02x%02x%02x" % (0, 0, dim),
        4: "0x%02x%02x%02x" % (0, dim, dim),
        5: "0x%02x%02x%02x" % (dim, 0, dim),
        6: "0x%02x%02x%02x" % (dim, dim, 0),
    }
    return int(switcher.get(i),16)

def dimbutton(channel):
    Col["dim"] += 20
    if Col["dim"] > 255:
        Col["dim"] = 0

def colorbutton(channel):
    Col["RGB"] += 1
    if Col["RGB"] == 7:
        Col["RGB"] = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(23, GPIO.RISING, callback=dimbutton)
GPIO.add_event_detect(24, GPIO.RISING, callback=colorbutton)
#GPIO.add_event_detect(25, GPIO.RISING, callback=reboot)

def Visual(LedValue):

    strip.clear_strip()
    color = colorSwitcher(Col["RGB"],Col["dim"])
    strip.set_pixel_rgb(24, color)
    strip.set_pixel_rgb(26, color)
    strip.set_pixel_rgb(49, 0x220000)
    strip.set_pixel_rgb(0, 0x220000)
    strip.set_pixel_rgb(LedValue, color)
    strip.show()
    # strip.cleanup()

def animate(i):
    fig = plt.figure()
    camera = Camera(fig)
    # plotting points as a scatter plot
    plt.scatter(i, 0, label="Cabel", color="green",
                marker="o", s=30)
    camera.snap()
    # x-axis label
    plt.xlabel('x - axis')
    plt.xlim(-0.5,0.5)
    # frequency label
    plt.ylabel('y - axis')
    # plot title
    plt.title('Point')
    # showing legend
    plt.legend()

    animation = camera.animate()
    animation.save('celluloid_minimal.gif')
    # function to show the plot

