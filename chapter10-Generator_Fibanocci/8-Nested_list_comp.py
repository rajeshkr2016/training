#'''
my_list = []

for x in [20, 40, 60]:
    for y in [2, 4, 6]:
        my_list.append(x * y)

#print(my_list)


my_list = [x * y for x in [20, 40, 60] for y in [2, 4, 6]]
print(my_list)

'''
List comprehensions allow us to transform one list or other sequence into a new list. 
They provide a concise syntax for completing this task, limiting our lines of code.

'''