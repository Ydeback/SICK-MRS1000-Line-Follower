# Main file of Communication for data receival from MRS1000c

from packets import *

# System start, Startup.py
connect()
loadConfig()
run()
global pos
pos = np.double([0, 0, 0, 0])
while True:
    # Take input from the device
    data = receive()

    # Preprocess the received data
    header = decodeDatagram(data)
    angle = getAngle(header)
    #print(data)
    #print(angle)
    #print(header["Data"])
    #print(header["NumberOfData"])
    #print(header["StartingAngle"])
    #print(header["AngularStepWidth"])
    #print(header["StopAngle"])
    layer = layerCheck(header)
    data = lengthFilter(header)
    if len(set(data)) == 1:
        pos[layer] = 99
    else:
        pos = position(data, layer, angle, pos)
    if np.all((pos)):
        print('Position for all layers',pos)
        pos = one_pos_all_layer(pos)

    # Filter the preprocess the data
    # filtering()

    # Analyze the filtered data
    # analysis()

    # Postprocessing of the analyzed data
    # Postprocess()

    # Visualize the postprocessed data
    # visual()
