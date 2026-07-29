#!/usr/bin/python3
"""Module with a function to check subclass inheritance."""


def inherits_from(obj, a_class):
    """Return True if obj inherits from a_class (directly or indirectly)."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
