#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return None
    dupl_list = list(my_list)

    new_list = [replace if x == search else x for x in dupl_list]
    return new_list
