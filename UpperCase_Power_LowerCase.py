import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

upper = sum(1 for char in s if char.isupper())
lower = sum(1 for char in s if char.islower())

print(upper**lower)
