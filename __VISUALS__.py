# Initialization of attribute and methods for the visuals methodset.

# Module for methods to handle the led strip
from apa102_pi.driver import apa102 
# Module to handle I/O on the Raspberry Pi
import RPi.GPIO as GPIO
# Module for time
import time
# Attribute to represent the rebootstate of the system
from __MAIN__ import flags


# Attribute to represent the number of leds to be used in the led strip
nleds = 93
# Attribute to represent the start color of the position led (1: Red, 2: Green, 3: Blue)
startcolor = 2
# Attribute to represent the led strength at the startup (range: 0 (dark), 255 (Bright))
startdim = 40 
# Attributes to set the autodimming mode at startup (bool: True (on),False (off)
startauto = False
startLED = True
# Attribute to set the amount of dim increase of the dim button
diminc = 20
# Attributes to adjust the external light sensor range
sensormax = 180
sensormin = 0
sensorspan = sensormin - sensormax

##### FIXED #####
# Object to represent the led strip
strip = apa102.APA102(num_led = nleds, order='rgb')
# Tuple to hold the visualisation attributes
Col = {}
# Attribute to represent which color the leds is set to from the start
Col["RGB"] = startcolor
# Attribute to represent the level of brightness on the leds
Col["DIM"] = startdim
# Flag to represent if the system is set to auto dimming mode
Col["AUTO"] = startauto
# Flag to identify if the system is in startup mode
Col["START"] = startLED
# Flag to identify if the system is set to reboot mode
flags["REBOOT"] = False
# Attributes to represent the dim range for the autodim method
ledmin = 5
ledmax = 255
ledspan = ledmax - ledmin
# Attribute to represent the previous led position
last_x = 1
