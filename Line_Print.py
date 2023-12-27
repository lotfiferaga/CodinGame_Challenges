import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
list = []
for i in range(n):
    x = int(input())
    list.append(x)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
sum = 0
for i in range(n):
    sum += list[i]

print(sum)
