# Main file of Communication of data from MRS1000c

from packets import *

# System start
startup()
print("Startup done!")

while True:
    # Take input from the device
    data = client()
    print("client done!")
    # Preprocess the received data
    preprocess(data)
    print("Preprocess done!")
    # Filter the preprocess the data
    # filtering()

    # Analyze the filtered data
    # analysis()

    # Postprocessing of the analyzed data
    # Postprocess()

    # Visualize the postprocessed data
    # visual()
