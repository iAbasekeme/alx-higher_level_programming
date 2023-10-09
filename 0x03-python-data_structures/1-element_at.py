def element_at(my_list, idx):
    if idx < 0 or idx is None or idx > len(my_list):
        return None
    else:
        index = my_list[idx]
    return index
