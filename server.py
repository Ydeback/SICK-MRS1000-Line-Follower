import socket

LiDARHOST = "LiDAR IP"
LiDARPORT = 2112
CLIENTHOST = socket.gethostname()
CLIENTPORT = 2113

#Creating socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # Binding
    try:
        s.bind((LiDARHOST,LiDARPORT))
    except socket.error:
        print("Bind to LiDAR failed")

    try:
        s.bind((CLIENTHOST,CLIENTPORT))
    except socket.error:
        print("Bind to Client failed")
    
    # Connect
    s.listen()
    lidar, lidaradress = s.accept()
    print("Connection from {adress} has been made!")
    client, clientadress = s.accept()
    print("Connection from {adress} has been made!")
    
    # Recieve data
    while True:
        data = s.recv(1024)
        if not data:
            print("No data received")
            break
        client.send(data)
print("Closing!...)
sleep(2)
s.close()
