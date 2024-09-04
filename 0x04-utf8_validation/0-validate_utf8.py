#!/usr/bin/python3
""" 0-validate_utf8.py """


def validUTF8(data):
    """ validUTF8 function
    """

    byte_count = 0

    first_bit_mask = 1 << 7
    second_bit_mask = 1 << 6

    for value in data:
        leading_bit_mask = 1 << 7

        if byte_count == 0:
            while leading_bit_mask & value:
                byte_count += 1
                leading_bit_mask >>= 1

            if byte_count == 0:
                continue

            if byte_count == 1 or byte_count > 4:
                return False
        else:
            if not (value & first_bit_mask and not (value & second_bit_mask)):
                return False

        byte_count -= 1

    return byte_count == 0
