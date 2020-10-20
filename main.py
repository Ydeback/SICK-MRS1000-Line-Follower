# Main file of Communication for data receival from MRS1000c

from packets import *

# System start
connect()
loadConfig()
run()

while True:
    # Take input from the device
    data = receive()

    # Preprocess the received data
    print(data)
    header = decodeDatagram(data)
    angle = angle()
    

    # Filter the preprocess the data
    # filtering()

    # Analyze the filtered data
    # analysis()

    # Postprocessing of the analyzed data
    # Postprocess()

    # Visualize the postprocessed data
    # visual()
