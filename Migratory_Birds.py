#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    unique_type = list(set(arr))
    unique_n = len(unique_type)
    type_dic = {}
    
    for i in range(0, unique_n):
        tmp_key = unique_type[i]
        tmp_value = 0
        type_dic[tmp_key] = tmp_value
    
    arr_n = len(arr)
    for i in range(0, arr_n):
        for j in range(0, unique_n):
            tmp_arr_mem = arr[i]
            tmp_type = unique_type[j]
            if(tmp_arr_mem == tmp_type):
                type_dic[tmp_type] = type_dic[tmp_type] + 1

    max_type_value = max(type_dic.values())
    candi = []
    for i in type_dic.keys():
        tmp_val = type_dic[i] 
        if(tmp_val == max_type_value):
            candi.append(i)
    
    result = min(candi)
    return result
                
    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
