#!/usr/bin/python3
"""Module that prints a name."""


def say_my_name(first_name, last_name=""):
    """Prints "My name is <first_name> <last_name>".

    Args:
        first_name: string, the first name
        last_name: string, the last name (default "")

    Raises:
        TypeError: if first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
