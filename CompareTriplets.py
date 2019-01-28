#!/bin/python

import math
import os
import random
import re
import sys


# Complete the compareTriplets function below.=
def compareTriplets(a, b):
    # aitem = ""
    # bitem = ""
    p_alice = 0
    p_bob = 0
    for ai in range(len(a) - 1):
        print("AI:",ai)
        for bi in range(len(b) - 1):
            if (ai==bi):
                if (a[ai] > b[bi]):
                    p_alice += 1
                    print("Alice:",p_alice)
                if (b[bi] > a[ai]):
                    p_bob += 1
                    print("Bob:",p_bob)

    arr = []
    arr.append(p_alice)
    arr.append(p_bob)
    return (arr)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a=[17,28,30]
    b=[99,16,8]

    # a = map(int, raw_input().rstrip().split())
    #
    # b = map(int, raw_input().rstrip().split())

    result = compareTriplets(a, b)
    print(result)
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()