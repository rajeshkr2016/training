'''
Decision making is required when we want to execute a code only if a certain condition is satisfied.

In Python, the body of the if statement is indicated by the indentation.
Body starts with an indentation and the first unindented line marks the end.

'''

# If the number is positive, we print an appropriate message

num = 3
if num > 0:
    print(num, "is a positive number.")
#print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")

print("This is also always printed.")


# else if


# Program checks if the number is positive or negative
# And displays an appropriate message

num = 3

# Try these two variations as well.
# num = -5
# num = 0

if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")


if num >= 0:
    print("Positive or Zero")
elif num < 0:
    print("Negative number")