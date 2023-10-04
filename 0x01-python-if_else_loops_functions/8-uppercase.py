#!/usr/bin/python3
def uppercase(str):
    uppercased_string = ''
    for i in str:
        # check if the character is a lowercase
        if ord(i) >= 97 and ord(i) <= 122:
            # convert to uppercase
            uppercase_char = chr(ord(i) - ord('a') + ord('A'))
        else:
            uppercase_char = i  # Keep non-lowercase characters unchanged
        # Append the uppercase character to the result string
        uppercased_string += uppercase_char
    print("{}".format(i), end="")


print("")
