#https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    maxnumber = max(arr)
    minnumber = min(arr)
    sum_num = sum(arr)
    print(sum_num - maxnumber, sum_num - minnumber)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
