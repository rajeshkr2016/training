'''
map(function, sequence) calls function(item) for each of the sequence’s items and returns a list of the return values.
For example, to compute some cubes:
'''

def cube(x):
    return x*x*x

result= list(map(cube, range(1, 10)))
print(result)


numList1=[1,2,3,4,5,6]
numList2=[7,8,9,10,11,12]

def add(x, y):
    return x+y

result= list(map(add, numList1, numList2))
print(result)
