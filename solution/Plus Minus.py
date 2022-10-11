#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    p = z = n = 0
    l = len(arr)
    for i in range(0, l):
        if arr[i] > 0:
            p += 1
        elif arr[i] < 0:
            n += 1
        else:
            z += 1
    print(round(p / l, 6))
    print(round(n / l, 6))
    print(round(z / l, 6))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
