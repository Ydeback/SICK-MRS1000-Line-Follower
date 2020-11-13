# Main file of Communication for data receival from MRS1000c
import time
from packets import *

time.sleep(5)
# System start, Startup.py

connect(s)
header = loadconfig()
FLAG = failCheck(header)
run(s)
global pos
pos = np.double([0, 0, 0, 0])
length = np.double([0, 0, 0, 0])
cabel_angle = np.double([0, 0, 0, 0])
t = time.time()


# Device ip-address
HOST = "169.254.93.123"

# Commication port
PORT = 2112

# Create Address for the device
ADDRESS = (HOST, PORT)


while True:
    if rebootFLAG[0]:
        rebootFLAG[0] = False
        reboot(s)
    elif rebootFLAG[1]:
        try:
            s.send(b'\x02sRN SCdevicestate\x03')
        except socket.error as err:
            s.close()
            s = createSocket()
            connect(s)
            run(s)
            rebootFLAG[1] = False
    else:
        data = receive(s)

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
        #print(data)
        # If we get no hit set value to 99
        if len(set(data)) == 1:
            pos[layer] = 99
        else:
            # analysis -> position
            pos, index1, cabel_angle = position(data, layer, angle, pos, cabel_angle)
            length = lengtharray(data, layer, index1, length)

        # All values from layers are collected
        if np.all((pos)):
            #print('Position for all layers', pos)
            #print('Length for all layers', length)
            #print('Angle for all layers', cabel_angle)

            sensor = light_sensor()
            autoLight()



            pos, pos_after_check, i = pos_layersafety(pos)

            #print('Position after all layer are checked:', pos_after_check, 'm')
            #print('Length after all layer are checked:', length[i], 'm')
            #print('Angle after all layer are checked:', cabel_angle[i], 'rad')

            led = convertposition_to_led(pos_after_check, length[i], cabel_angle[i], header)
            #print('LED:', led)

            visual(led)

