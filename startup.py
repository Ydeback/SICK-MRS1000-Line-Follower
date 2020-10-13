#Startup configuration of MRS1000c LiDAR

#ifndef windows
#ifndef linux
#ifndef mac


HOST = "169.254.93.123" # Device ip-address
PORT = 2112 # Commication port
ADDRESS = (HOST,PORT) # Create Address for the device
START_ANGLE = 0.08726646259 # Temporary value of start angle (horz)(rad)
STOP_ANGLE = -0.08726646259 # Temporary value of stop angle (horz)(rad)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def load_config(): # Loading the config of the MRS1000c LiDAR 
    pass

def connect(): # Connect to the LiDAR
    
    try:
        s.connect(ADDRESS)
        print("Connected to:", HOST)
    except socket.error as error:
        print("Connection failed: ", error)

    pass

def startup(): # Load config and connect to LiDAR
    load_config()
    connect()
