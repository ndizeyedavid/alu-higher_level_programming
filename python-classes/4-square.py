#!/usr/bin/python3
"""Module defining a Square class with getter and setter for size."""


class Square:
    """Represents a square with property getter/setter for size."""

    def __init__(self, size=0):
        """Initialize a new Square with optional size.

        Args:
            size: The size of the square (must be int >= 0).
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value: The new size (must be int >= 0).

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
