#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10 ;
if number < 0:
    digit = digit * -1
if digit < 0:
    print(f"Last digit of {number} is {digit:d} and is less than 6 and not 0")
elif digit > 0:
    if digit <= 5:
        print(f"Last digit of {number} is {digit:d} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {digit:d} and is greater than 5")
else:
    print(f"Last digit of {number} is 0 and is 0")
