""" This utilities file holds important (and hopefully reusable) functions for 
    the Matasano Cryptopals challenges.
"""

##** Constants

# This table contains a list of the hexadecimal character values
HEX_TABLE = [
    "0", "1", "2", "3", "4", "5", "6", "7", 
    "8", "9", "a", "b", "c", "d", "e", "f"
]

# This table contains a list of the base64 encoding character values.
BASE_64_TABLE = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", 
    "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", 
    "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", 
    "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", 
    "4", "5", "6", "7", "8", "9", "+", "/"
]

##** Functions

def hex_to_base64(hex_string):
    """ This function takes a hexadecimal string for input and converts it to 
        base64.

        http://en.wikipedia.org/wiki/Base64
    """

    # Validate input
    for char in hex_string:
        if char not in HEX_TABLE:
            raise ValueError('found %c in hexadecimal string input' % char)

    # Build a list of the hex bytes
    size = len(hex_string)
    bytes = map(lambda x: int(x, base=16), hex_string)
    base_64 = list()

    for index in range(2, size - (size % 3), 3):

        """ Grab three bytes to compute into two base64 characters:

            bytes:  |_______|_______|_______|
            bits:   |_|_|_|_|_|_|_|_|_|_|_|_|
            base64: |___________|___________|

        """

        base_64.append(bytes[index - 2] << 2 | bytes[index - 1] >> 2)
        base_64.append((bytes[index - 1] & 3) << 4 | bytes[index])

    if size % 3 == 1:
        """ One trailing byte:

            bytes:  |_______|
            bits:   |_|_|_|_|0|0|
            base64: |___________|
        """

        base_64.append(bytes[size - 1] << 2)

        
    elif size % 3 == 2:
        """ Two trailing bytes:

            bytes:  |_______|_______|
            bits:   |_|_|_|_|_|_|_|_|0|0|0|0|
            base64: |___________|___________|
        """

        base_64.append(bytes[size - 2] << 2 | bytes[size - 1] >> 2)
        base_64.append((bytes[size - 1] & 3) << 4)

    return ''.join(map(lambda index: BASE_64_TABLE[index], base_64))
