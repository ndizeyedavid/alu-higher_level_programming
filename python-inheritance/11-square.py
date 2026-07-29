#!/usr/bin/python3
"""Module defining a Square class with custom string representation."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square with [Square] <width>/<height> representation."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: Positive integer size.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the square description: [Square] <width>/<height>."""
        return "[Square] {}/{}".format(self.__size, self.__size)
