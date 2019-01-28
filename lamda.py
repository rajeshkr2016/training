'''
cube = []
for x in range(10):
    cube.append(x**3)
print(cube)
In lambda x: x**3; x is an arguments to the function
and x**3 is the expression which gets executed
and its values is returned as output.
'''

cubes = list(map(lambda x: x**3, range(10)))
print(cubes)


'''
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
'''

