# Filtering of the measured data and adjusting the configurations

from __FILTERING__ import *

# Filter the distances to only care for the specified interval
# @return the data filtered for the distance threshold
def lengthFilter(data):
    data = np.array(data)
    data[data > upper] = 99
    data[data < lower] = 99
    return data
