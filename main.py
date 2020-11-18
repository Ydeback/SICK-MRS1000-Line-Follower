# Main file of Communication for data receival from MRS1000c
from packets import *
from __MAIN__ import *

s = startup()
strip.clear_strip()
while True:
    # If the reboot button has been pushed, reboot the LiDAR.
    if flags["REBOOT"]:
        # Run reboot procedure of the LiDAR,
        # also connected to Reboot.py, also rebooting Raspberry Pi.
        reboot(s)
    else:
        # Receive data from the LiDAR, @return binary data stream
        data = receive(s)
        #if(len(data) > 30):
        # Preprocess the received data, @return data split into named
        # sections
        header = decodeDatagram(data)
        # @return array of individual laser angles corresponding
        # to the received data points
        angle = getAngle(header)

        # @return which scan layer the sent data belongs to
        layer = layerCheck(header["Layer"])
        # @return the data stream filtered to prescribed interval
        filtered = lengthFilter(header["Data"])
        # If we get no hit set value to 99
        if len(set(filtered)) == 1:
            pos[layer] = 99
        else:
            # @return pos: position?
            # @return index: the index of the?
            # @return cableangle: ?
            pos, index, cableangle = position(filtered, layer, angle, pos, cableangle)
            # @return ?
            length = lengthArray(filtered, layer, index, length)
        # If all values from the four scan layers are collected
        if np.all((pos)):
            # @return pos: ?
            # @return posaftercheck: ?
            # @return i: ?
            pos, posaftercheck, hitlayer = pos_layersafety(pos)

            # @return Which led in the led strip the position is
            # represented by
            led = convertPositionToLed(posaftercheck, length[hitlayer], cableangle[hitlayer], header)
            # Update the led strip with the correct position
            # representation
            visual(led)


