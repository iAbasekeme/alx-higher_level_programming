#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        # this is possible because max operates on values
        max_values = max(a_dictionary)
    if max_values is None:
        return None
    else:
        return max_values
