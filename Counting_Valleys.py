#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    new_list =list(s)
    numericlist = []
    for i in new_list:
        if i == 'D':
            numericlist.append(-1)
        else:
            numericlist.append(1)
    
    sum_up = 0
    valley = 0
    for j in numericlist:
        if sum_up == -1 and j == 1:
            valley += 1
        sum_up += j
    return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

