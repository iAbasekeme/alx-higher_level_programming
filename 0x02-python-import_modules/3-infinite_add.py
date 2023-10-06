#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sum_of_digits = 0
    args = sys.argv[1:]
    for i in args:
        sum_of_digits += int(i)
    print("{:d}".format(sum_of_digits))
