def upperacse(c):
    uppercased_string = ''  # initialize an empty string to store the uppercase version
    for i in c:
        if ord(i) >= 97 and ord(i) <= 122:  # check if the character is a lowercase
            # convert to uppercase
            uppercase_char = chr(ord(i) - ord('a') + ord('A'))
        else:
            uppercase_char = i  # Keep non-lowercase characters unchanged
        # Append the uppercase character to the result string
        uppercased_string += uppercase_char
    return uppercased_string  # Return the uppercase string
