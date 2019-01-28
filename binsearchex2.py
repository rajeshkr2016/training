def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1
	return found

A=[1,2,3,5,8]
x=6

print(binary_search(A,x))


A=[1,2,3,5,8]
x=5
print(binary_search(A,x))