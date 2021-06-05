##############################################
# 2D Lists is a list where each item in that list is another list, and that list represents the items in each row.
"""
3x3 Matrix
[
    1 2 3
    4 5 6
    7 8 9
] """
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[0][1] = 20
print("2D", matrix[0][1])
matrix[0][1] = 2


# Use of nested loops to iterate over all the items.
for row in matrix:
    for element in row:
        print(element)

