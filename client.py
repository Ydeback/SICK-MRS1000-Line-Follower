# Input the data from the device in raw binary format

from startup import s

BUFFER = 2068

def receive():
    return s.recv(BUFFER)

def client():
    return receive()
    print("Message stored")
