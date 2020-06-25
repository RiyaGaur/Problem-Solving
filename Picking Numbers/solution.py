import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    arr = sorted(a)
    cnt = []
    for i in range(len(arr)):
        c = 0
        for j in range(i,len(arr)):
            if(abs(arr[i]-arr[j])<=1):
                c+=1
        cnt.append(c)
    return max(cnt)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
