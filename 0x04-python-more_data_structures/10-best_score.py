#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        # this is possible because max operates on values
        # for each key key=a_dictionary.get is used to extract the associated value from the dictionary
        max_values = max(a_dictionary, key=a_dictionary.get)
    try:
        if max_values is None:
            return None
    except:
        return None
    else:
        return max_values
