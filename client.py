# Input the data from the device in raw binary format
from startup import s

BUFFER = 2048

# Receive data sent from device
def receive(s):
    return s.recv(BUFFER)

