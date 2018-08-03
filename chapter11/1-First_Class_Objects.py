'''
In Python, functions are first-class objects.
This means that functions can be passed around, and used as arguments,
just like any other value (e.g, string, int, float).
'''

def func(bar):
    return bar + 1

print(func)
print(func(2))
print(type(func))


def call_func_with_arg(func, arg):
    return func(arg)
a=call_func_with_arg(func, 3)
print(a)
