'''
Python also allows you to return functions from other functions
'''

def parent_func(num):

    def first_child_func(num1, num2):
        return num1+num2

    def second_child_func():
        return "Printing from the second_child_func() function."

    try:
        assert num == 10
        return first_child_func
    except AssertionError:
        return second_child_func

foo = parent_func(10)
#bar = parent_func(11)

print(foo)
#print(bar)

print(foo(5,6))
#print(bar())

# Note:  we executed the sibling functions within the parent functions.
# In this example, we did not add parenthesis to the sibling functions first_child_func or second_child_func

'''
When it encounters an assert statement, Python evaluates the accompanying expression, which is hopefully true. 
If the expression is false, Python raises an AssertionError exception. 
The syntax for assert is − assert Expression[, Arguments]

'''