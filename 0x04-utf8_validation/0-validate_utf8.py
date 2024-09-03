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
        mask_byte = 1 << 7
        if num_bytes == 0:
            while mask_byte & i:
                num_bytes += 1
                mask_byte = mask_byte >> 1

            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (i & mask1 and not (i & mask2)):
                return False
        num_bytes -= 1

    if num_bytes == 0:
        return True
    return False
