"""

age = int(input("enter age: "))
size = input("enter the size of each candle: ")
l = size.split()
l.sort()
l.reverse()
print(l)
count = 1
for j in range(age-1):
    if l[j] == l[j+1]:
        count += 1
    elif l[j] != l[j+1]:
        break
print(count)
"""




"""
age = (input())
size = input()
l = size.split()
l.sort()
l.reverse()
count = 1
for j in range(age-1):
    if l[j] == l[j+1]:
        count += 1
    elif l[j] != l[j+1]:
        break
print(count)
"""

"""
age = input()
size = input()
n = max(size)
count = 0
for i in size:
    if i == n:
        count += 1
print(count)


"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(ar):
    # Write your code here
    k = max(ar)
    count = 0
    for i in ar:
        if i == k:
            count += 1
    return(count)    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
    