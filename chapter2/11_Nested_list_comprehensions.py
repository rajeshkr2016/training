#Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4:

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]


print("Before Transpose of matrix")
print(matrix)

print("After Transpose of matrix - with regular")
transposed = []
for i in range(4):
    print("Value of i : ", i)
    transposed_row = []
    for items in matrix:
        print("Row : ", items, " index : ", i)
        transposed_row.append(items[i])
        print(transposed_row)
    transposed.append(transposed_row)
print(transposed)



print("After Transpose of matrix - with list comprehension")
tranMatix=[[row[i] for row in matrix] for i in range(4)]
print(tranMatix)
