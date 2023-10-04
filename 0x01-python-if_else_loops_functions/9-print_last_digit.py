#!/usr/bin/python3
def print_last_digit(number):
    if number == 0:
        end_digit = 0
    else:
        end_digit = int(str(number)[-1])
    print("{:d}".format(end_digit), end="")
    return end_digit
