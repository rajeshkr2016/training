# Python3 code to demonstrate list
# concatenation using naive method

# Initializing lists
test_list1 = [1, 4, 5, 6, 5]
test_list2 = [3, 5, 7, 2, 5]
mergedlist=[]
# using naive method to concat
# for j in test_list1:
for i in test_list2:
          # if i > j:
          #     mergedlist.append(j)
          #     mergedlist.append(i)
          #
          test_list1.append(i)

# Printing concatenated list
print("Concatenated list using native method : "
      + str(test_list1))

for index in range(1, len(test_list1)):
    current = test_list1[index]
    position = index
    print("Initial Position:" + str(position))
    print("Intial TestList:"+str(test_list1))

    while position > 0 and test_list1[position - 1] > current:
        print("Position:"+str(position))
        print("Swapped {} for {}".format(test_list1[position], test_list1[position - 1]))
        test_list1[position] = test_list1[position - 1]
        print(test_list1)
        position -= 1

    test_list1[position] = current

# Printing concatenated list
print("Concatenated sorted list using native method : "
      + str(test_list1))