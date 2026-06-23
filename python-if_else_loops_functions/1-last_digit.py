#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10 if number >= 0 else -(-number % 10)
result = ""

if last_digit > 5:
    result = "greater than 5"
elif last_digit == 0:
    result = "0"
elif last_digit < 6:
    result = "less than 6 and not 0"
print(f"Last digit of {number} is {last_digit} and is {result}")
