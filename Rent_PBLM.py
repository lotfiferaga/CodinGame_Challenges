import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

p = int(input())
h = int(input())
r = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
cost = p*h 

if  cost > r: 
    print("YES")
elif cost == r  :
    print("BARELY")
else :
    print("NO")
