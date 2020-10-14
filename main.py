# Main file of Communication of data from MRS1000c

from packets import *

# System start
startup()

# Take input from the device
input()

# Preprocess the received data
preprocess()

# Filter the preprocess the data
filter()

# Analyze the filtered data
analysis()

# Postprocessing of the analyzed data
Postprocess()

# Visualize the postprocessed data
visual()
