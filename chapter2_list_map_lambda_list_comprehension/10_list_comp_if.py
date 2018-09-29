'''

A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.
For example, this listcomp combines the elements of two lists if they are not equal:
'''
print("Generating List combo with regular method")
list1=[1,2,3]
list2=[3,1,4]

combs = []
for x in list1:
    for y in list2:
        if x !=y:
            combs.append([x,y])
print(combs)


print("Generating List combo with list comprehension")
combs1=[[x, y] for x in list1 for y in list2 if x != y]
print(combs1)