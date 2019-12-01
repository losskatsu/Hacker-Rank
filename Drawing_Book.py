#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    if(n%2 ==0):
        n_turn = int(n/2) + 1
    else:
        n_turn = int(n/2 - 0.5) + 1

    result1 = n
    for i in range(0, n_turn):
        current_page = (2*i)+1
        if( (p == current_page) | (p == current_page - 1) ):
            result1 = i
              
    
    result2 = n
    for i in range(0, n_turn):
        current_page = n - (2*i)
        if(n%2 == 0):
            if((p == current_page) | (p == current_page + 1)):
                result2 = i                      
        else:
            if((p == current_page) | (p == current_page - 1)):
                result2 = i
            
    
    result = min(result1, result2)            

    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
