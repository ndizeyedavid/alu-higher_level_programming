#!/usr/bin/python3
"""Module defining a Square class with private size attribute."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size):
        """Initialize a new Square with a given size.

        Args:
            size: The size of the square's side.
        """
        self.__size = size
