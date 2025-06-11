#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Get the last digit
the_last_digit = abs(number) % 10
if number < 0:
    the_last_digit = -the_last_digit
# Determine the condition
if the_last_digit > 5:
    condition = "greater than 5"
elif the_last_digit == 0:
    condition = "0"
else:
    condition = "less than 6 and not 0"
# Print the result
print(f"Last digit of {number} is {the_last_digit} and is {condition}")
