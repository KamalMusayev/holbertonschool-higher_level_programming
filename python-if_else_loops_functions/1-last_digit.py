#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

if last_digit > 5:
    print(f"{number} is greather than 5")
elif last_digit == 0:
    print(f"{number} and is 0")
else:
    print(f"{number} and is less than 6 and not")
