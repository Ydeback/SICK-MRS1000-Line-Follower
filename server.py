import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),15200))
s.listen(5)

while True:
    clientsocket, adress = s.accept()
    print(f"Connection from {adress} has been made!")
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))


