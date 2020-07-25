# In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

# Function Description

# Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.

# aVeryBigSum has the following parameter(s):

# int ar[n]: an array of integers .

# Return

# int: the sum of all array elements
# Input Format

# The first line of the input consists of an integer .
# The next line contains  space-separated integers contained in the array.

# Output Format

# Return the integer sum of the elements in the array.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    c = 0
    for i in range(ar_count):
        c = c+ar[i]
    return c
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
