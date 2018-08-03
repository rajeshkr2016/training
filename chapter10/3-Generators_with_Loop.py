'''
Normally, generator functions are implemented with a loop having a suitable terminating condition.
Let's take an example of a generator that reverses a string
'''
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1,-1,-1):
        yield my_str[i]

# For loop to reverse the string
for char in rev_str("hello world"):
    print(char)