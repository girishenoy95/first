# Playing around with 2D Lists and Nested Loops

number_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


for row in number_list:
    for column in row:
        print(column, end=" ")
    print()

# The output is
#  1 2 3
#  4 5 6
#  7 8 9


