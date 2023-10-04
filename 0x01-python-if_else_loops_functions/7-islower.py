#!/usr/bin/python3
def islower(c):
    if str(ord(c)) >= '97' or str(ord(c)) <= '122':
        return True
    elif str(ord(c)) >= '65' or str(ord(c)) <= '90':
        return False
