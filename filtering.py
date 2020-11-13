# Filtering of the measured data and adjusting the configurations
import numpy as np

def lengthFilter(header):
    # Filter the distances to only care for the specified interval
    high_threshold = 5
    low_threshold = 0.1
    data = np.array(header["Data"])

    data[data > high_threshold] = 99
    data[data < low_threshold] = 99
    return data