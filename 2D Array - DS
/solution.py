#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def getRow(n):
    if n < 4: return 0
    elif n < 8: return 1 
    elif n < 12: return 2
    else: return 3
    
def getColumn(n):
    if n < 4: return n
    else: return n - (4*getRow(n))

    
def getTop(n, arr):
    row = getRow(n)
    col = getColumn(n)
    return arr[row][col:col+3]

def getMid(n, arr):
    row = getRow(n) + 1
    col = getColumn(n)
    return [0, arr[row][col+1], 0]
    
def getBottom(n, arr):
    row = getRow(n) + 2
    col = getColumn(n)
    return arr[row][col:col+3]
    
def getGlassSum(i, arr):
    glass = []
    glass.append(getTop(i, arr))
    glass.append(getMid(i, arr))
    glass.append(getBottom(i, arr))
    return sum(sum(glass, []))
    
def hourglassSum(arr):
    # Write your code here
    max = getGlassSum(0, arr)
    for i in range(1,16):
        glass = getGlassSum(i, arr)
        if glass > max: max = glass
        
    return max
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

