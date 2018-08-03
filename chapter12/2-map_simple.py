'''
map functions expects a function object and any number of iterables like list, dictionary, etc.
It executes the function_object for each element in the sequence and returns a list of the elements modified by the function object.
'''


def multiply2(x):
    return x * 2

output=set(map(multiply2,[1, 2, 3, 4]))

#output=list(map(multiply2,[1, 2, 3, 4]))

print(output)
