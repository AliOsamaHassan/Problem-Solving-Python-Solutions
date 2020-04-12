"""
Problem Link: https://www.hackerrank.com/challenges/migratory-birds/
"""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    types_counts = [0, 0, 0, 0, 0, 0]
    for i in range(len(arr)):
        types_counts[arr[i]] += 1
    return types_counts.index(max(types_counts))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()

