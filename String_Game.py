import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

o = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

if o == "Scissors" : 
    print("Stone")

elif o == "Stone" : 
    print("Hand")

elif o == "Hand" : 
    print("Scissors")

else : 
    print("Error")
