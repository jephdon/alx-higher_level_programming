#!/usr/bin/python3

def roman_to_int(roman_string):
    # Check if the input is valid
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Define the Roman numeral values
    roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

    # Initialize variables
    total = 0
    prev_value = 0

    # Loop through the string backwards
    for char in reversed(roman_string):
        value = roman_values.get(char, 0)

        # Add or subtract based on the previous value
        if value >= prev_value:
            total += value
        else:
            total -= value

        # Update the previous value for the next iteration
        prev_value = value
    return total
