#!/usr/bin/python3
import sys

if __name__ == "__main__":
    lengt = len(sys.argv[1:])
    if lengt == 0:
        print("0 arguments.")
    elif lengt == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(lengt))
    i = 1
    lengt = 1
    for i in sys.argv[1:]:
        print("{}: {}".format(lengt, i))
        lengt += 1
