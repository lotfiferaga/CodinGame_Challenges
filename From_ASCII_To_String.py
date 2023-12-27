import sys
import math 

value_count = int(input())
string_values = []

for value in input().split():
    try:
        # Convert hexadecimal input to integer
        decimal_value = int(value, 16)
        string_values.append(chr(decimal_value))
    except ValueError:
        print(f"Error: '{value}' is not a valid hexadecimal value.")

# Print the resulting string
resulting_string = ''.join(string_values)
print(resulting_string)
