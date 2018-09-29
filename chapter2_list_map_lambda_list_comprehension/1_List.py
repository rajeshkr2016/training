'''

1. Lists are one of the most powerful tools in Python.
2. They are just like the arrays declared in other languages, but the most powerful thing is that list need not be always homogeneous.
   A single list can contain strings, integers, as well as objects.
3. Lists can also be used for implementing stacks and queues.
4. Lists are mutable, i.e., they can be altered once declared.

'''

# Declaring and printing list
L = [1, "a", "string", 1 + 2]
print(L)

# Adding more items
L.append(6)
print(L)

# Removing an item
L.pop()
'''
Remove the item at the given position in the list, and return it. 
If no index is specified, a.pop() removes and returns the last item in the list. 
(The square brackets around the i in the method signature denote that the parameter is optional, 
not that you should type square brackets at that position.)
'''
print(L)

# Printing a particular item
print(L[1])

# Return the index in the list of the first item whose value is x.
print(L.index('a'))

# number of times a appears in the list.
print(list.count('a'))

# Sort the items of the list in place
newList=[8,1,90,23,12,67,100,2,]
newList.sort()
print(newList)

# Reverse the elements of the list, in place.
newList.reverse()
print(newList)

'''
You might have noticed that methods like reverse, sort that only modify the list have no return value printed – they return the default None. 
This is a design principle for all mutable data structures in Python.
'''

# create list
shoppingList =["Apple","Orange","Banana","cheese"]

# print with index id
print(shoppingList[0])

print(shoppingList[1:3])

#Append an item list
shoppingList.append("Blue berry")
print(shoppingList[0:])

#update list with an item
shoppingList[3]="Cherries"
print(shoppingList[0:])

#delete an item
del shoppingList[4]
print(shoppingList[0:])

#get length of list
print(len(shoppingList))

#Number list
newNumList=[1,4,2,8,11,9,20]
print(min(newNumList))
print(max(newNumList))
print(sum(newNumList))
