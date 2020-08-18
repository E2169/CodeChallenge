'''
Here is the solution to the Hackerrank Challenge named 'Compare the Triplets'
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    score = [0, 0]
    for a, b in zip(a, b):
        if a > b:
            score[0]+= 1
        elif b > a:
            score[1]+=1
    return score


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


