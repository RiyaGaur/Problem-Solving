import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def factor(i,a):
    
    for j in a:
        if i%j == 0:
            pass
        else:
            return False
    return True

def factor2(i,b):
    
    for j in b:
        if j%i == 0:
            pass
        else:
            return False
    return True

def getTotalX(a, b):
    a_list1 = []
    a_factor_list1 = []
    b_factor_list1 = []

    for i in range(a[0],b[0]+1):
        a_list1.append(i)
    
    for i in a_list1:
        if(factor(i,a)):
            a_factor_list1.append(i)

    for i in a_factor_list1:
        if(factor2(i,b)):
            b_factor_list1.append(i)
      
    
    
    return len(b_factor_list1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
