#!/usr/bin/python3
"""Module with a function to check exact class instance."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class."""
    return type(obj) is a_class
