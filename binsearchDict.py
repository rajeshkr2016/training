def binary_search(item_dict,item):
    first = 0
    last = len(item_dict)-1
    print("last:",last)

    found = False
    while( first<=last and not found):
        mid = (first + last)//2
        if item_dict[mid] == item :
            found = True
        else:
            if item < item_dict[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

A={'a':1,'b':2,'c':3,'d':5,'e':8}
x=6

print(binary_search(A,x))


A=[1,2,3,5,8]
x=5
print(binary_search(A,x))