# Visualisation to the LEDs
# from apa102_pi.driver import apa102
# strip = apa102.APA102(num_led=50, order='rgb')
# Strip.clear_strip()
#strip.set_pixel_rgb(6, 0xFF0000)

# Led = list(range(1, 12))
# PantografWidth = list(range(-2000, 2000))



#strip.set_pixel_rgb(LedValue, 0xFF0000)
#strip.show()
#strip.cleanup()
#NewMax = 10
#NewMin = 0
#pantografMin = -2000
#pantografMax = 2000

#PantogradfRange = (pantografMax - pantografMin)
#LedRange = (NewMax - NewMin)
#NewValue = (((OldValue - pantografMin) * LedRange) / PantografRange) + NewMin

leftMin = -2000
leftMax = 2000
rightMin = 0
rightMax = 10
value =

#translate(value, leftMin, leftMax, rightMin, rightMax):
# Figure out how 'wide' each range is
leftSpan = leftMax - leftMin
rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
led = rightMin + (valueScaled * rightSpan)
print(led)