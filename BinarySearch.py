## https://github.com/krsrini/learnPython

def binSearch(ary, elem):
    def recurse(first, last):
        if first > last:
            return None
        mid =int( (first + last) / 2)

        if (ary[mid] < elem):
            return recurse(mid + 1, last)
        elif (ary[mid] > elem):
            return recurse(first, mid - 1)
        else:
            return mid

    return recurse(0, len(ary)-1)



ar=[1,2,3,45,6,7]
ele=45

xout=binSearch(ar,ele)

print(xout)