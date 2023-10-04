#!/usr/bin/python3
for i in range(0, 9):
    for u in range(i + 1, 10):        
        if i != u:
            print("{}{}".format(i,u),end=", " if i < 8 or u < 9 else "\n")        
