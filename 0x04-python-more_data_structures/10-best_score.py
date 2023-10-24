#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if not a_dictionary:
        return None
        # this is possible because max operates on values
        # for each key=a_dictionary.get is used to extract
        # the associated value from the dictionary
    max_values = max(a_dictionary, key=a_dictionary.get)
    return max_values
