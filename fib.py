#recurrsive
# big O notation = O(n^2)
def fiboRec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fiboRec(n-1)+fiboRec(n-2)

#iter
# big O notation = O(n)
def fibIter(n):
    a=0
    b=1
    result=[0]
    for i in range(0,n):
        a, b = b, a+b
        result.append(a)

    return a

result = fibIter(6)
print("Iterative Method :",result)

result1 = fiboRec(6)
print("Reccursive Method :", result1)
# 0,1,1,2,3,5