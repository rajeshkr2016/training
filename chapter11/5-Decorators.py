def my_decorator(some_function,num):

    def wrapper():

        if num == 10:
            print("Yes!")
        else:
            print("No!")

        some_function()
        print("Something is happening after some_function() is called.")

    return wrapper

def just_some_function():
    print("Wheee!")

just_some_func1 = my_decorator(just_some_function, 10)

just_some_func1()