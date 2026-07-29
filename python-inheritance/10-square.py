#!/usr/bin/python3
"""Module defining a Square class inheriting from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class with size validation."""

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
