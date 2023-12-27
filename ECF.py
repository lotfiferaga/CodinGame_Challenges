import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    e = int(input())
    if n >= 2 and n <= 9 :
        if e >= 2 and e <= 300 :
            print(int(e * 7.5 + 700))
