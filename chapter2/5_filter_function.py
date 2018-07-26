'''
filter(function, sequence) returns a sequence consisting of those items from the sequence for which function(item) is true
'''

# define a function
def func(n):
    return n % 3 == 0 or n % 5 == 0

list1=[]
for i in range(2, 25):
    #print(i, func(i))
    if func(i):
        list1.append(i)

print("result from for loop", list1)

res = list(filter(func, range(2, 25)))

print("result from filter", res)
