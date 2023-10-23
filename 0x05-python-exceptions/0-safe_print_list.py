#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """A function that prints x elements of a list"""
    try:
        count = 0
        for i in my_list:
            if count >= x:
                break
            print(i, end="")
            count += 1
        print()
    except Exception as e:
        print("An error occurred:{}", format(e))
    return count
