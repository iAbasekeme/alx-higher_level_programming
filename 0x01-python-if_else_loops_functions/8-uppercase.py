#!/usr/bin/python3
def uppercase(str):
    for i in str:
        # check if the character is a lowercase
        if ord(i) >= 97 and ord(i) <= 122:
            # convert to uppercase
            uppercase_char = chr(ord(i) - ord('a') + ord('A'))
    print("{}".format(uppercase_char), end=" ")
