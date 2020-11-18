# Initialization of attribute and methods for the visuals methodset.

# Module for methods to handle the led strip
from apa102_pi.driver import apa102 
# Module to handle I/O on the Raspberry Pi
import RPi.GPIO as GPIO
# Module for named tuples
from collections import namedtuple as nt
# Module for time
import time
# Attribute to represent the rebootstate of the system
from __INIT__ import flags


# Attribute to represent the number of leds to be used in the led strip
nleds = 93
# Attribute to represent the start color of the position led (1: Red, 2: Green, 3: Blue)
startcolor = 2
# Attribute to represent the led strength at the startup (range: 0 (dark), 255 (Bright))
startdim = 0
# Attribute to set the autodimming mode at startup (bool: True (on),False (off)
startauto = True
startLED = False
# Attribute to set the amount of dim increase of the dim button
diminc = 40
# Attribute to adjust the external light sensor range
sensormax = 180
sensormin = 0
sensorspan = sensormin - sensormax

##### FIXED #####
# Object to represent the led strip
strip = apa102.APA102(num_led = nleds, order='rgb')
# Named tuple to store led attributes
NamedTuple = nt("Colors", ["RGB", "DIM", "AUTO", "START", "LIGHT"])
# Tuple to hold the named tuple attributes
Col = {}
Col["RGB"] = startcolor
Col["DIM"] = startdim
Col["AUTO"] = startauto
Col["START"] = startLED
Col["LIGHT"] = 0
# Attributes to represent the dim range for the autodim method
ledmin = 5
ledmax = 255
ledspan = ledmax - ledmin
# Flag to identify if the system is set to reboot mode
flags["REBOOT"] = False

