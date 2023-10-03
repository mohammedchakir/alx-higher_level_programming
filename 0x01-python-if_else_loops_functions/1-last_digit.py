#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = abs(number) % 10

if last_digit > 5:
    message = "greater than 5"
elif last_digit == 0:
    message = "0"
else:
    message = "less than 6 and not 0"
if number < 0:
    message = "negative " + message
print(f"Last digit of {number} is {last_digit} and is {message}")
