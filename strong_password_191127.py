#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    need_num = 0
    special_char = "!@#$%^&*()-+"
    n_sc = len(special_char)
    min_num = 6-n

    tmp_res = 0
    for i in range(0, n):    
        if(password[i].isnumeric() == True):
            tmp_res = tmp_res + 1
            break
    if(tmp_res == 0):
        need_num = need_num + 1

    tmp_res = 0
    for i in range(0, n):    
        if(password[i].isupper() == True):
            tmp_res = tmp_res + 1
            break
    if(tmp_res == 0):
        need_num = need_num + 1

    tmp_res = 0
    for i in range(0, n):    
        if(password[i].islower() == True):
            tmp_res = tmp_res + 1
            break
    if(tmp_res == 0):
        need_num = need_num + 1
    
    tmp_res = 0
    for i in range(0, n_sc):
        if(special_char[i] in password):
            tmp_res = tmp_res + 1
            break
    if(tmp_res == 0):
        need_num = need_num + 1

    need_num = max(need_num, min_num)
    
    return need_num
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
