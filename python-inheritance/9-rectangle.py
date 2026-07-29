#!/usr/bin/python3
"""Module defining a Rectangle class with area and string representation."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle with area calculation and string representation."""

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

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description: [Rectangle] <width>/<height>."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
