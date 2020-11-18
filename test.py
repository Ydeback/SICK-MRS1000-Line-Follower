
from apa102_pi.driver import apa102

import RPi.GPIO as GPIO

import time

strip = apa102.APA102(1, order='rgb')

GPIO.setmode(GPIO.BCM)

while True:
    # Set the I/O for the pin to output
    GPIO.setup(25, GPIO.OUT)
    # Set the output mode to LOW
    GPIO.output(25, GPIO.LOW)
    # Set pin mode to input
    GPIO.setup(25, GPIO.IN)
    # Get the current time
    currentTime = time.time()
    # Reset the time difference attribute
    diff = 0
    
    # While the input is LOW, get the time difference
    while (GPIO.input(25) == GPIO.LOW):
        diff = time.time() - currentTime
    print(round(diff * 100000))
