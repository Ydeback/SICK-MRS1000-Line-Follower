#!/bin/bash
# Run the main code of the line follower program, write the terminal output and the error log to the file main.log
python3 /home/pi/Desktop/BolidenCodes/main.py >> /home/pi/Desktop/main.log 2>&1 & 
# Run the reboot code of the line follower program, write the terminal output and the error log to the file reboot.log
python3 /home/pi/Desktop/BolidenCodes/reboot.py >> /home/pi/Desktop/reboot.log 2>&1 & 
