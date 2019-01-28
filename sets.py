# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)


# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')

# unique letters in a
print("set a : ", a)
print("set b : ", b)

# letters in a but not in b
print(" a minus b : ", a - b)

# letters in a or b or both
print(" a union b :", a | b)

# letters in both a and b
print("a intersection b : ",  a & b )

# letters in a or b but not both
print(a ^ b)

#Similarly to list comprehensions, set comprehensions are also supported:
z = {x for x in a if x not in 'abc'}
print(z)