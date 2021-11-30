#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    valleys = 0
    hasEnteredValley = False
    timesTravelled = 0
    for step in path:
        
        # update location
        if step == 'U': valleys += 1
        elif step == 'D': valleys -= 1

        
        # check if entered valley
        if valleys < 0: hasEnteredValley = True
        
        # check if left valley
        if valleys >= 0 and hasEnteredValley: 
            timesTravelled += 1
            hasEnteredValley = False
        
        print(valleys, hasEnteredValley, timesTravelled)
        
    return timesTravelled
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

