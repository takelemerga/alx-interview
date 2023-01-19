#!/usr/bin/python3
"""
Log parsing
"""
import sys


def print_statistics(file_size, status_codes):
    """
    displays stats
    """
    print("File size: {}".format(file_size))
    codes_sorted = sorted(status_codes.keys())
    for code in codes_sorted:
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


status_code_dict = {'200': 0, '301': 0, '400': 0, '401': 0,
                    '403': 0, '404': 0, '405': 0, '500': 0}

file_size_total = 0
number_of_lines = 0

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            try:
                line = line.replace("\n", "")
                status_code = line.split()[-2]
                if status_code in status_code_dict.keys():
                    status_code_dict[status_code] += 1
                file_size = int(line.split()[-1])
                file_size_total += file_size
            except Exception:
                pass
            number_of_lines += 1
            if number_of_lines % 10 == 0 and number_of_lines > 0:
                print_statistics(file_size_total, status_code_dict)
    except KeyboardInterrupt:
        print_statistics(file_size_total, status_code_dict)
        raise
