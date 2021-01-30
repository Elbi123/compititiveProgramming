#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.


def countingSort(arr):
    count = [0] * 101
    output = []
    for i in range(len(arr)):
        count[arr[i]] += 1

    for i in range(len(count)):
        while count[i] > 0:
            output.append(i)
            count[i] -= 1
    return output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
