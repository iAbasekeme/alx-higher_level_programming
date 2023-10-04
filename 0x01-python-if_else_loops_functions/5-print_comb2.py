#!/usr/bin/python3
for num in range(100):
    formatted_input = "{:02}".format(num)
    if num < 99:
        print("{}".format(formatted_input), end=", ")
    else:
        print("{}".format(formatted_input))
