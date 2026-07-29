#!/usr/bin/python3
"""Module that prints a square with the character #."""


def print_square(size):
    """Prints a square of size `size` using the # character.

    Args:
        size: integer, the side length of the square

    Raises:
        TypeError: if size is not an integer, or if size is a float < 0
        ValueError: if size is less than 0
    """
    if isinstance(size, bool) or not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
