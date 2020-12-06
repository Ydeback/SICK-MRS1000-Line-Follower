# Methodset and initialization file for the testmode procedures.

import os, datetime

# Attribute to set the testmode
# 1 = Layer, Array of distances, (bool) if there was a hit or miss of the layer 
# 2 = Distance of hit object, offset of hit object, and positional led number
# 3 = Remission values, intensity values
# 

path1 = r"/home/pi/Desktop/CaseOne/"
path2 = r"/home/pi/Desktop/CaseTwo/"
path3 = r"/home/pi/Desktop/CaseThree/"
timepath = r"/home/pi/Desktop/rebootTime.txt"
filename1 = ""
filename2 = ""
filename3 = ""
start = [True, True, True]

def rebootTime():
    filename = timepath
    f = open(filename,"a")
    f.write(datetime.datetime.now().strftime("%c")+"\n")
    f.close()


def fileName(target):
    TARGET_DIR = target 
    n = sum(1 for f in os.listdir(TARGET_DIR) if os.path.isfile(os.path.join(TARGET_DIR, f)))
    return "{}file_{}.txt".format(TARGET_DIR,n+1)


def writeFile(filename, *args):
    f = open(filename,"a")
    for arg in args:
        f.write(str(arg)+",")
    f.write("\n")
    f.close()


def fname(path, case):
    if case == 1:
        if start[0]:
            global filename1
            filename1 = fileName(path)
        return filename1
    if case == 2:
        if start[1]:
            global filename2
            filename2 = fileName(path)
        return filename2
    if case == 3:
        if start[2]:
            global filename3
            filename3 = fileName(path)
        return filename3

def testOne(*args):
    filename = fname(path1,1)
    start[0] = False
    writeFile(filename, *args) 

def testTwo(*args):
    filename = fname(path2,2)
    start[1] = False
    writeFile(filename, *args) 


def testThree(*args):
    filename = fname(path3,3)
    start[2] = False
    writeFile(filename, *args) 


