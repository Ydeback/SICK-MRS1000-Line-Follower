# Main file of Communication for data receival from MRS1000c

from packets import *

# System start, Startup.py
connect()
loadConfig()
run()
while True:
    # Take input from the device
    data = receive()

    # Preprocess the received data
    print(data)
    header = decodeDatagram(data)
    angle = getAngle(header)
    print(angle)
    print(header["Data"])
    print(header["NumberOfData"])
    print(header["StartingAngle"])
    print(header["AngularStepWidth"])
    print(header["StopAngle"])
    layer = layerCheck(header)
    data = lengthFilter(header)
    pos = position(data, layer, angle)
    print(pos)

    # Filter the preprocess the data
    # filtering()

    # Analyze the filtered data
    # analysis()

    # Postprocessing of the analyzed data
    # Postprocess()

    # Visualize the postprocessed data
    # visual()
