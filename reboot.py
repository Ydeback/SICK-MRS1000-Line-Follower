import os
import RPi.GPIO as GPIO
import time

def reboot(channel):
    time.sleep(2)
    os.system("sudo shutdown -r now")


GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(8, GPIO.RISING, callback=reboot, bouncetime=300)

while True:
    pass
