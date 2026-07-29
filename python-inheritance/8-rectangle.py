#!/usr/bin/python3
"""Module defining a Rectangle class inheriting from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class with width and height validation."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width: Positive integer width.
            height: Positive integer height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
