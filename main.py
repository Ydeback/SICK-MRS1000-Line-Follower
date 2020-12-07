from client import *
from preprocess import *
from filtering import *
from analysis import *
from postprocess import *
from visuals import *
from testmode import *
from __MAIN__ import *

####
# Test case three, remove in final
rssiarray = {}
indexarray = {}

def main():

    ####
    # Part of test, remove in final
    rebootTime()
    ####

    global pos
    global length
    global cableangle
    # Run the system startup procedure
    s = startup()
    while True:
        # If the reboot button has been pushed, reboot the LiDAR.
        if flags["REBOOT"]:
            # Run reboot procedure of the LiDAR,
            # also connected to Reboot.py, also rebooting Raspberry Pi.
            reboot(s)
        else:
            
            # Receive data from the LiDAR, @return binary data stream
            data = receive(s)
            
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
                
                # @return pos: Offset distance from the centre of the LiDAR
                # @return index: The scan point index of the layer
                # @return cableangle: the angle of the same scan index
                pos, index, cableangle = position(filtered, layer, angle, pos, cableangle)
                
                # @return Array of the length of the hits from each layer
                length = lengthArray(filtered, layer, index, length)
                
                ####
                # Test case three, remove in final
               
                if remang == b'1':
                    rssi = header["RSSI"]
                    rssiarray[layer] = rssi[index]
                ####

            # If all values from the four scan layers are collected
            if np.all((pos)):
                

                ####
                # test case one, remove in final
                # testOne(length, flags["MISS"]) 
                ####
                
                # @return pos: The reset offset distance array for next run
                # @return posaftercheck: The offset distance from all the
                # chosen layer to represent the hit
                # @return hitlayer: The hit layer that the position is taken from
                pos, posaftercheck, hitlayer = posLayerSafety(pos)
                


                # @return Which led in the led strip the position is
                # represented by
                led = convertPositionToLed(posaftercheck, length[hitlayer], cableangle[hitlayer], header)
                
                ####
                # test case two, remove in final
                # testTwo(posaftercheck, led)
                ####

                ####
                # Test case three, remove in final
                if remang == b'1':
                    testThree(sorted(rssiarray.items()), hitlayer, length[2])
                    # print(sorted(rssiarray.items()), hitlayer, length[2])
                ####

                ####
                # Test case four, remove in final
                # testFour(posaftercheck, led, length[hitlayer], hitlayer)
                ####

                # Update the led strip with the correct position
                visual(led)

if __name__ == '__main__':
    main()
    
