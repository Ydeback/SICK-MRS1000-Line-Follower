import socket

HOST = socket.gethostname()
PORT = 2113

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    
    # Connect
    s.connect((HOST, PORT))
    
    # Receive data
    while True:
    data = s.recv(1024)
    print("Received: ", repr(data)"\n")
