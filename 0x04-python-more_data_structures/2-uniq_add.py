#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return None
    rey = set(my_list)
    ret = sum(rey)
    return ret
