#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10
str = "Last digit of "
if number < 0:
    digit = ((-1 * number) % 10) * -1
if digit < 0:
    print(f"{str}{number} is {digit:d} and is less than 6 and not 0")
elif digit > 0:
    if digit <= 5:
        print(f"{str}{number} is {digit:d} and is less than 6 and not 0")
    else:
        print(f"{str}{number} is {digit:d} and is greater than 5")
else:
    print(f"{str}{number} is 0 and is 0")
