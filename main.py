# Main file of Communication for data receival from MRS1000c

from packets import *

global pos = np.double([0, 0, 0, 0])
t = time.time()

# System start, Startup.py
connect()
loadConfig()
run()

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

    # Preprocess -> layerCheck
    layer = layerCheck(header)
    # filtering -> lengthFilter
    data = lengthFilter(header)

    # If we get no hit set value to 99
    if len(set(data)) == 1:
        pos[layer] = 99
    else:
        # analysis -> position
        pos = position(data, layer, angle, pos)
        #print(pos)

    # All values from layers are collected
    if np.all((pos)):
        #print('Position for all layers',pos)

        # analysis -> pos_layersafety
        pos, i = pos_layersafety(pos)
        print('Position after all layer are checked:', i, 'm')
        # postprocess -> convertposition_to_led
        led = convertposition_to_led(i)
        print('LED:', led)

        # analysis -> output_time
        t = output_time(t)

    # Filter the preprocess the data
    # filtering()

    # Analyze the filtered data
    # analysis()

    # Postprocessing of the analyzed data
    # Postprocess()

    # Visualize the postprocessed data
    # visual()
