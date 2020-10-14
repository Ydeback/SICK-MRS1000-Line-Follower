# Input the data from the device in raw binary format

BUFFER = 256

def receive():
    while True:
        data = socket.recv(BUFFER)
        for byte in data:
            yield bytes([byte])
def input():
    received = receive()
