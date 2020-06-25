from collections import Counter
import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    num_odd = 0
    s1 = Counter(s)
    for each in s1.values():
        if each % 2 != 0:
            num_odd += 1
            if num_odd > 1:
                return 'NO'
    return ('YES')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
