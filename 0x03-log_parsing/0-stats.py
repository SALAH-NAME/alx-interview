#!/usr/bin/python3
""" 0-stats.py """
import sys


def print_stats(total_size, status_counts):
    """print_stats"""
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")


file_size = 0
code = 0
line_count = 0
codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            line_count += 1

            if line_count <= 10:
                file_size += int(parsed_line[0])
                code = parsed_line[1]

                if (code in codes.keys()):
                    codes[code] += 1

            if (line_count == 10):
                print_stats(codes, file_size)
                line_count = 0

finally:
    print_stats(codes, file_size)
