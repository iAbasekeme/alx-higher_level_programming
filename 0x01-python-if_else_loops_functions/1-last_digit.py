#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number % 10
if num > 5:
	print(f'Last digit of {number:d} is {num:d} and is greater than 5\n')
elif num == 0:        
	print(f'Last digit of {number:d} is {num:d} and is 0\n')
else:       
	print(f'Last digit of {number:d} is {num:d} and is less than 6 and not 0\n')    
