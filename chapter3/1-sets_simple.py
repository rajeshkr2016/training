
'''
A set is created by placing all the items (elements) inside curly braces {},
separated by comma or by using the built-in function set().

It can have any number of items and they may be of different types
(integer, float, tuple, string etc.).
But a set cannot have a mutable element, like list, set or dictionary, as its element.
'''
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)