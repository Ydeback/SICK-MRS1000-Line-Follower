import os
import RPi.GPIO as GPIO
import time

def reboot(channel):
    time.sleep(3)
    os.system("sudo shutdown -r now")

### Uncomment the lines starting with GPIO for enabling the reboot button
### functionality
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.add_event_detect(24, GPIO.FALLING, callback=reboot, bouncetime=350)

# Let the program run indefinitely
while True:
    pass
