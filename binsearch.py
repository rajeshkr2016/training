# Binary search needs to be sorted
#

def binarySearch(searchList,startIndex, endIndex, searchitem):

    if startIndex> endIndex:
        return -1

    mid = int((endIndex-startIndex)/2)

    if searchList[mid]==searchitem:
        return mid
    elif searchList[mid] > searchitem:
        return binarySearch(searchList, startIndex , mid-1, searchitem)
    elif searchList[mid]< searchitem:
        return binarySearch(searchList, mid+1 , endIndex, searchitem)

A=[10,15,19,22,27,30,50,99,100,150,655]
X=655

binaryRes=binarySearch(A,0,len(A), X)
print(binaryRes)

