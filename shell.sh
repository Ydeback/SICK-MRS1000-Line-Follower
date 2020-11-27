#!/bin/bash
python3 /home/pi/Desktop/BolidenCodes/main.py >> /home/pi/Desktop/main.log 2>&1 & 
python3 /home/pi/Desktop/BolidenCodes/reboot.py >> /home/pi/Desktop/reboot.log 2>&1 & 
