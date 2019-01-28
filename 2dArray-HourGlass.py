# #!/bin/python
#
# import math
# import os
# import random
# import re
# import sys
#
# # Complete the hourglassSum function below.
#
# def hourglassSum(arr):
#     sumt = 0
#     for i in range(4):
#         for j in range(4):
#             sumt = sum(arr[i][j:j + 3] + [arr[i + 1][j + 1]] + arr[i + 2][j:j + 3])
#             maxv = max(sumt)
#     return (maxv)
#

def hourglassSum(arr):
    sum = []

    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            sum.append(arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] +
                       arr[i + 2][j + 2])

    return(max(sum))



if __name__ == '__main__':

    arr = []
    arr=[[1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]]


    result = hourglassSum(arr)

    print(result)


