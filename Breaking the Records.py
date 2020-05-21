#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max_count=0
    min_count=0
    max1=scores[0]
    min1=scores[0]
    for i in range(1,n):
        if scores[i]<min1:
            min1=scores[i]
            min_count+=1
    for i in range(1,n):
        if scores[i]>max1:
            max1=scores[i]
            max_count+=1
    return max_count,min_count        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
