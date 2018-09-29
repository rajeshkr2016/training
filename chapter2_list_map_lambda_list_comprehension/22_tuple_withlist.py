# Tuples are immutable:
tup1=(1,2,3,4,5)
print(tup1[1])
#tup1[1]=5

#but they can contain mutable objects:
tup2 = ([1, 2, 3], [3, 2, 1])
print(tup2)
print(tup2[0])
print(tup2[0][0])

#update list inside tuple
tup2[0][0]=9
print(tup2)
