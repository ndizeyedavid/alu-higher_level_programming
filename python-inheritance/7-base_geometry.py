#!/usr/bin/python3
"""Module defining a BaseGeometry class with integer validator."""


class BaseGeometry:
    """Base geometry class with area method and integer validator."""

    def area(self):
        """Raise an exception indicating area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name="", value=None):
        """Validate that value is a positive integer.

        Args:
            name: The name of the value (assumed to be a string).
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
