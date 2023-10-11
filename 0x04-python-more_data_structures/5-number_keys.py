#!/usr/bin/python3
def number_keys(a_dictionary):
    if not a_dictionary:
        return None

    ker = a_dictionary.keys()
    return len(ker)
