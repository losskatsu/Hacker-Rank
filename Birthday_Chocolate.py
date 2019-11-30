#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    n = len(s)
    result = 0
    
    for i in range(0, n):
        n1 = 0
        count = 0
        while(n1 < m):
            count = count + s[i + n1]
            n1 = n1 + 1
        if(count == d):
            result = result + 1
        if(i+n1==n):
            break
    
    return result

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
