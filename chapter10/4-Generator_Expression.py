'''
Same as lambda function creates an anonymous function,
generator expression creates an anonymous generator function.
'''

# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
op1= [x**2 for x in my_list]
print(op1)


# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
genOp1 = (x**2 for x in my_list)
print(genOp1)

print(next(genOp1))
print(next(genOp1))
print(next(genOp1))
print(next(genOp1))

# Output: StopIteration
#next(genOp1)
