import collections

MRS1000 = collections.namedtuple("MRS1000_Datagram",
        ["TypeOfCommand", "Command", "VersionNumber", "DeviceNumber", "SerialNumber", "DeviceSatus1", "DeviceSatus2", "TelegramCounter", "ScanCounter", "TimeSinceStartup", "TimeOfTransmission", "InputStatus1", "InputStatus2", "OutputStatus1", "OutputStatus2", "ScanningFrequency", "MeasurementFrequency", "NumberOfEncoders", "NumberOf16bitChannels", "MeasuredDataContents", "ScalingFactor", "ScalingOffset", "StartingAngle", "AngularStepWidth", "NumberOfData", "Data"]) # "NumberOf8BitChannels", # "Position", # "Name", # "Comment", # "TimeInformation", # "EventInformation"])

def decode_datagram(datagram):
    items = datagram.split(b' ')

    header = {}
    header['TypeOfCommand'] = items[0].decode('ascii')
    if header['TypeOfCommand'] != 'sSN':
        return None
    header['Command'] = items[1].decode('ascii')
    if header['Command'] != 'LMDscandata':
        return None
    header['VersionNumber'] = dist(items[2])
    header['DeviceNumber'] = dist(items[3])
    header['SerialNumber'] = items[4].decode('ascii')
    header['DeviceStatus1'] = dist(items[5])
    header['DeviceStatus2'] = dist(items[6])
    if header['DeviceStatus1'] != 0 or header['DeviceStatus2'] != 0:
        return None
    header['TelegramCounter'] = dist(items[7])
    header['TimeSinceStartup'] = dist(items[9])
    header['TimeOfTransmission'] = dist(items[10])
    header['AngularStepWidth'] = dist(items[24])
    header['NumberOfData'] = dist(items[25])
    header['Data'] = [dist(x) / 1000 for x in items[26:26+header['NumberOfData']]]

    return header

def dist(length):
    if b'+' in length or b'-' in length:
        return int(length)
    else:
        return int(length, 16)

def from_socket(socket):
    while True:
        data = socket.recv(256)
        for byte in data:
            yield bytes([byte])

def datagrams_from_socket(socket):
    STX = b'\x02'
    ETX = b'\x03'

    data = from_socket(socket)

    while True:
        datagram = b''

        for byte in data:
            if byte == STX:
                break

        for byte in data:
            if byte == ETX:
                break
            datagram += byte
        yield datagram
