# File for initialization of variables for the main class

import time
import numpy as np

pos = np.double([0, 0, 0, 0])
length = np.double([0, 0, 0, 0])
cableangle = np.double([0, 0, 0, 0])
t = time.time()

# Variable to assign the accepted buffer size for communications 
BUFFER = 2048
# Startup flag if the program is booting
