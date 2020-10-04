import socket

HOST = socket.gethostname()
PORT = 2112

#Creating socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding
try:
    s.bind((HOST,PORT))
except socket.error:
    print("Bind failed")

# Connect to client
s.listen(5)
client, adress = s.accept()
print(f"Connection from {adress} has been made!")

# Recieve data
while True:
    data = s.recv(1024)
    print(data.decode("ASCII")"\n")
    

