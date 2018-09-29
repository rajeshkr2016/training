'''
The for loop that is used to iterate over elements of a sequence, it is often
used when you have a piece of code which you want to repeat "n" number of time.

It works like this: " for all elements in a list, do this "
'''

computer_brands = ["Apple", "Asus", "Dell", "Samsung"]
i=0
for brands in computer_brands:
    #increment operator
    i += 1
    print("Brand :",i, brands)

''' 
for n in range(2, 25):
    print(n)
'''