#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.


def maximumToys(prices, k):
    total = 0
    items = 0
    for i in range(len(prices)):
        for j in range(i):
            if prices[i] < prices[j]:
                temp = prices[i]
                prices[i] = prices[j]
                prices[j] = temp
    for i in prices:
        total += i
        if total < k:
            items += 1
    return items


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
