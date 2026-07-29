#!/usr/bin/python3
"""Module with a function to check class or inheritance."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is instance of a_class or a subclass thereof."""
    return isinstance(obj, a_class)
