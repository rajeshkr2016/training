'''
Python allows you to simplify the calling of decorators using the @ symbol (this is called “pie” syntax).
'''


from decorator07 import my_decorator_func


@my_decorator_func
def just_some_function():
    print("Wheee!")

just_some_function()

'''
So, @my_decorator_func is just an easier way of saying 
just_some_function = my_decorator(just_some_function).
 It’s how you apply a decorator to a function.
'''
