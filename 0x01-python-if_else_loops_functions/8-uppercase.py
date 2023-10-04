def upperacse(c):    
    uppercased_string = '' #initialize an empty string to store the uppercase version
    for i in c:        
        if ord(i) >= 97 and ord(i) <= 122: # check if the character is a lowercase
            uppercase_char = chr(ord(i) - ord('a') + ord('A')) # convert to uppercase
        else:
            uppercase_char = i # Keep non-lowercase characters unchanged
        uppercased_string += uppercase_char # Append the uppercase character to the result string
    return uppercased_string # Return the uppercase string