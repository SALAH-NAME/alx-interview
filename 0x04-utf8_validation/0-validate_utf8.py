#!/usr/bin/python3
""" 0-validate_utf8.py """


def validUTF8(data):
    """
    valid_utf8 function
    """
    num_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        byte = num & 0xFF

        if num_bytes == 0:
            if (byte & mask1) == 0:
                continue
            elif (byte & (mask1 >> 1)) == mask1:
                num_bytes = 1
            elif (byte & (mask1 >> 2)) == (mask1 >> 1):
                num_bytes = 2
            elif (byte & (mask1 >> 3)) == (mask1 >> 2):
                num_bytes = 3
            else:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False
        num_bytes -= 1

    return num_bytes == 0
