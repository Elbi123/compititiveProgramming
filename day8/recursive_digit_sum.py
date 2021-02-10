#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.


def superDigit(n, k):
    new_num = n * k
    total = 0
    for i in range(len(new_num)):
        total += int(new_num[i])
    return total


def rec_digit(n):
    new_num = str(n)
    total = 0
    if len(new_num) == 1:
        return int(n)
    for i in range(len(new_num)):
        total += int(new_num[i])
    return rec_digit(total)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = rec_digit(superDigit(n, k))

    fptr.write(str(result) + '\n')

    fptr.close()
