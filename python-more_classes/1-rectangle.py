#!/usr/bin/python3
"""Module defining a Rectangle class with width and height."""


class Rectangle:
    """Represents a rectangle with private width and height."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the current width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation.

        Args:
            value: Must be an integer >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the current height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation.

        Args:
            value: Must be an integer >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
