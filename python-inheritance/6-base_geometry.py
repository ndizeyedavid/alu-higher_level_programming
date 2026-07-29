#!/usr/bin/python3
"""Module defining a BaseGeometry class with area method."""


class BaseGeometry:
    """Base geometry class with an unimplemented area method."""

    def area(self):
        """Raise an exception indicating area is not implemented."""
        raise Exception("area() is not implemented")
