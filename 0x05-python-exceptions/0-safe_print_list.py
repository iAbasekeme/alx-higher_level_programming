#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """A function that prints x elements of a list"""
    try:
        rt = my_list[:x]
        count = 0
        for i in rt:
            print(i, end="")
            count += 1
        print()
        return count
    except IndexError:
        print("an Indexerror occured")
        return 0
