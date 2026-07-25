#!/usr/bin/python3
"""Module defining a Rectangle class with custom print symbol."""


class Rectangle:
    """Represents a rectangle with a customizable print symbol."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle and increment instance count.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the current width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation."""
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
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the rectangle perimeter. 0 if width or height is 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation using print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(
            str(self.print_symbol) * self.__width for _ in range(self.__height)
        )

    def __repr__(self):
        """Return a string that recreates the instance via eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Decrement instance count and print goodbye message."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
