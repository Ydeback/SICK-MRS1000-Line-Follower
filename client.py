# Input the data from the device in raw binary format

from __INIT__ import BUFFER

# Receive data sent from device
def receive(s):
    return s.recv(BUFFER)

