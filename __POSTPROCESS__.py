# Initialization file for the preprocessing methodset

#Import module for math functionality
import math

#Attributes to represent the range of the led strip
ledstart = 0
ledstop = 92
ledrange = ledstop - ledstart

# Attributes to represent the offset endpoints in metres,
# The values represents the endpoints of the offset shown as the endpoints on
# the LED-strip
# Both min and max positive: Only right side offset
# Both min and max negative: Only left side offset
# min negative and max positive: Offset field has endpoints on each side of the
# centre of the LiDAR 0 degree centre.
lidarmin = -0.92
lidarmax = -3
lidarspan = lidarmax - lidarmin

