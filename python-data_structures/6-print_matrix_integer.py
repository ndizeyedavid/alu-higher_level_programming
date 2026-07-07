#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for numbers in matrix:
        for number in numbers:
            print("{:d}".format(number), end=" ")
        print("\n")
