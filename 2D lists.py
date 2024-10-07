matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# index for the element 2; 0 is the index for the first inner list and 1 is the index of element 2 in that list
print(matrix[0][1])
print('---------')
for row in matrix:
    for item in row:
        print(item)
print('------------')
matrix[0][1] = 20    # replaces the element 2 with 20
print(matrix)
