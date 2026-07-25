#!/usr/bin/python3
"""Module defining a MagicClass that matches given bytecode."""

import math


class MagicClass:
    """Represents a circle with radius for area/circumference."""

    def __init__(self, radius=0):
        """Initialize MagicClass with radius validation.

        Args:
            radius: Must be an int or float.

        Raises:
            TypeError: If radius is not int or float.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference of the circle."""
        return 2 * math.pi * self.__radius
