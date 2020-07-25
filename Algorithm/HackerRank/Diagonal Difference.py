# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix  is shown below:

# 1 2 3
# 4 5 6
# 9 8 9  
# The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

# Function description

# Complete the  function in the editor below.

# diagonalDifference takes the following parameter:

# int arr[n][m]: an array of integers
# Return

# int: the absolute diagonal difference
# Input Format

# The first line contains a single integer, , the number of rows and columns in the square matrix .
# Each of the next  lines describes a row, , and consists of  space-separated integers .

# Constraints

# Output Format

# Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

import math
import os
import random
import re
import sys


# Complete the 'diagonalDifference' function below.

# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.


def diagonalDifference(arr):
    # Write your code here
    left_diagonal = 0 
    right_diagonal = 0 
    
    for i in range(len(arr[0])): 
        left_diagonal = left_diagonal + arr[i][i] 
        right_diagonal = right_diagonal + arr[i][len(arr[0])-i-1] 
        
    answer = abs(left_diagonal - right_diagonal) 
    
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()