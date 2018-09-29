'''
1. User-defined functions are reusable code blocks; they only need to be written once,
then they can be used multiple times. They can even be used in other applications, too.
2. These functions are very useful, from writing common utilities to specific business logic. These functions can also be modified per requirement.

'''
# Finding duplicate in list
def findDuplicate(list1):
	items=set(list1)
	result={}
	for item in items:
		if list1.count(item)>1:
			result[item]=list1.count(item)
	return result

list1=["A","B","C","D","A","B","A","X","M"]
print(findDuplicate(list1))

