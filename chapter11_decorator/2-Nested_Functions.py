'''
You can define functions inside other functions. Such functions are called nested functions.
'''

def parent_func():
    print("Printing from the parent_func() function.")

    def first_child_func():
        return "Printing from the first_child_func() function."


    def second_child_func():
        return "Printing from the second_child_func() function."

    print(first_child_func())
    print(second_child_func())


parent_func()

#first_child_func()
#You should get an error: