# Input the data from the device in raw binary format

from startup import s

BUFFER = 2068

# Receive data sent from device
def receive():
    return s.recv(BUFFER)

