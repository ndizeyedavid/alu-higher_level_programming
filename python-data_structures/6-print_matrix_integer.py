#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for numbers in matrix:
        for i  in range(len(numbers)):
            print("{:d}".format(numbers[i]), end=" " if i < len(numbers) - 1 else "")
        print()

atrix = [
    [1, 2],
    [4, 5]
]
print_matrix_integer(atrix)
