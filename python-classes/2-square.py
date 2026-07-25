#!/usr/bin/python3
"""Module defining a Square class with size validation."""


class Square:
    """Represents a square with validated private size."""

    def __init__(self, size=0):
        """Initialize a new Square with optional size validation.

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
