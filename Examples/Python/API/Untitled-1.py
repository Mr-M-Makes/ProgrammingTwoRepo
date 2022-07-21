import struct

def is_64_windows():
    """Find out how many bits is OS. """
    print(struct.calcsize('P') * 8 == 64)

is_64_windows()