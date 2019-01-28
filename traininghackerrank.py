# n = int(input())
# arr = list(map(int, input().split()))
# largest = max(arr)
#
# for i in range(n):
#     if largest == max(arr):
#         arr.remove(max(arr))
#
# print(max(arr))
from typing import List, Any, Union

if __name__ == '__main__':

    #n = int(n)
    arr=[10,8,5,5,10,10,11,14,14,11,12]
    n = len(arr)
    #arr = map(int, arr.split())

    #big = ""
    eerunnerup = ""
    big=max(arr)
    arr.pop(arr.index(big))
    #print(big)
    for i in range(n-1):
        if (eerunnerup == ""):
            eerunnerup = arr[i]
        # print(big)
        # print(big)
        # print(eerunnerup)
        #if (eerunnerup > arr[i]) and (eerunnerup!=big):

        if (arr[i] > eerunnerup) and (arr[i] != big):
            eerunnerup = arr[i]

    print(eerunnerup)
    #print (arr)
