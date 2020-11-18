# File for initialization of variables used by all files
from collections import namedtuple as nt

# Assigned value for the accepted buffer size of communications
BUFFER = 2048

# Named tuple, unmutable during runtime, to represent the naming conventions of the tuple flags to store
# the current values of the different flags of the system, the flags starting
# value is set in their corresponding initialization files corresponding
# to the methodset where they are first used.
NamedTuple = ("flags",["CONNECT", "REBOOT", "MISS", "CONFIG", "LOGIN", ])
# Mutable tuple to store the values of the different flags during runtime.
flags = {}
