#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findMedian function below.


def findMedian(arr):
    for i in range(1, len(arr)):
        item = arr[i]
        j = i - 1
        while j >= 0 and item < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = item

    if len(arr) % 2 != 0:
        # mid = len(arr) // 2
        return arr[len(arr)//2]
    elif len(arr) % 2 == 0:
        low = len(arr) // 2
        high = low + 1
        median = (low + high) // 2
        return arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
