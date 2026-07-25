#!/usr/bin/python3
"""Module defining a Square class with comparison operators."""


class Square:
    """Represents a square that can compare by area."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size: The size (must be a number >= 0).
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the current size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation.

        Args:
            value: The new size (must be a number >= 0).

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Return True if areas are equal."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Return True if areas are not equal."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Return True if area is less than other."""
        return self.area() < other.area()

    def __le__(self, other):
        """Return True if area is less than or equal to other."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Return True if area is greater than other."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Return True if area is greater than or equal to other."""
        return self.area() >= other.area()
