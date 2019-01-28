

def linearsearch(searchList,searchValue):
    print(searchList,searchValue)
    for i in range(len(searchList)):
        if (searchList[i]==searchValue):
            print ("found the value:",searchList[i],"at position:",i)

    #print("This is my first search")

A = [1, 2, 3, 4, 5, 6, 7, 8,9,10]
X = 8

linearsearch(A,X)

# for item in A:
    #     if (item == 8):
    #         print(item)
