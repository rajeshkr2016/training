'''
note : the value of variable n is remembered between each call.
Unlike normal functions, the local variables are not destroyed when the function yields.
Furthermore, the generator object can be iterated only once.
To restart the process we need to create another generator object using something like a = my_gen().
'''

# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

# It returns an object but does not start execution immediately.
a = my_gen()

# We can iterate through the items using next().
print(next(a))

# Once the function yields, the function is paused and the control is transferred to the caller.
# Local variables and theirs states are remembered between successive calls.
print(next(a))
print(next(a))

# Finally, when the function terminates, StopIteration is raised automatically on further calls.
try :
    print(next(a))
except:
    print("StopIteration error")