#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    unique = sorted(list(set(arr)))
    ele_count = []
    for uni_ele in unique:
        count = 0
        for arr_ele in arr:
            if(uni_ele == arr_ele):
                count += 1

        ele_count.append(count)

    return(unique[ele_count.index(max(ele_count))])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
