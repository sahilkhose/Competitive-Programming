#!/bin/python3

import math
import os
import random
import re
import sys
import datetime
from datetime import datetime as dt

# Complete the time_delta function below.
def time_delta(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    return str(int(abs((dt.strptime(t1, fmt) - dt.strptime(t2, fmt)).total_seconds())))
    # a = t1.split()
    # b = t2.split()
    # time1 = [int(ele) for ele in a[4].split(':')]
    # time2 = [int(ele) for ele in b[4].split(':')]

    # date_time1 = datetime.datetime(int(a[3]), datetime.datetime.strptime(str(a[2]), "%b").month, int(a[1]), time1[0], time1[1], time1[2])
    # date_time2 = datetime.datetime(int(b[3]), datetime.datetime.strptime(str(b[2]), "%b").month, int(b[1]), time2[0], time2[1], time2[2])

    # return str(int(abs((date_time1-date_time2 + datetime.datetime.strptime(str(a[-1]), "%z") - datetime.datetime.strptime(str(b[-1]), "%z")).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
