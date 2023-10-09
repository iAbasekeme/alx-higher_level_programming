def delete_at(my_list=[], idx=0):
    if not my_list:
        return None
    del my_list[idx]
    return my_list
