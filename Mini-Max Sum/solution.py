import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    sum=0
    for i in arr:
        sum+=i
    min=sum-arr[len(arr)-1]
    max=sum-arr[0]
    print(min,max)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
