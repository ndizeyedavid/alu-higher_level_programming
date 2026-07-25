#!/usr/bin/python3
"""Module defining a Square class with area calculation."""


class Square:
    """Represents a square that can calculate its area."""

    def __init__(self, size=0):
        """Initialize a new Square with optional size.

        Args:
            size: The size of the square (must be int >= 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
