# Methodset and initialization file for the testmode procedures.

from main import *
import os
# Attribute to set the testmode
# 1 = Layer, Array of distances, (bool) if there was a hit or miss of the layer 
# 2 = Distance of hit object, offset of hit object, and positional led number
# 3 = Remission values, intensity values
# 

testmode = 1

testStart = [True]
path = r"/Home/Desktop/"
filename = ""

def fileName(target, testStart):
    if testStart[0]:
        TARGET_DIR = target 
        n = sum(1 for f in os.listdir(TARGET_DIR) if os.path.isfile(os.path.join(TARGET_DIR, f)))
        global filename
        filename =  "{}\{}.txt".format(TARGET_DIR,n+1)
        testStart[0] = False
    return filename


def writeFile(filename, *args):
    f = open(filename,"a")
    for arg in args:
        f.write(str(arg)+",")
    f.write("\n")
    f.close()


def testOne(*args):
    filename = fileName(path+"/CaseOne", testStart)
    writeFile(filename, *args) 

def testTwo(*args):
    filename = fileName(path+"/CaseTwo", testStart)
    writeFile(filename, *args) 


def testThree(*args):
    filename = fileName(path+"/CaseThree", testStart)
    writeFile(filename, *args) 


# Switcher method for running the output method for the specified test
# procedure
def testOutput(i):
    switcher = {
            1: testOne(length, flags["MISS"]),
            2: testTwo(posaftercheck, led),
            3: testThree(header["RSSI"])
            }

while True:
    testOutput(testmode)


