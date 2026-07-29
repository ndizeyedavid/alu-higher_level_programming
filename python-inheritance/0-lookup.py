#!/usr/bin/python3
"""Module with a function to list object attributes and methods."""


def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    return dir(obj)
