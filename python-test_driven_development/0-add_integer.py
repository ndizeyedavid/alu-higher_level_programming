#!/usr/bin/python3
"""Module that adds two integers."""


def add_integer(a, b=98):
    """Adds two integers and returns the result.

    Args:
        a: first number, must be an integer or float
        b: second number, must be an integer or float, default 98

    Returns:
        int: the sum of a and b after casting floats to integers

    Raises:
        TypeError: if a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        if a != a or a == float('inf') or a == float('-inf'):
            raise TypeError("a must be an integer")
        a = int(a)
    if isinstance(b, float):
        if b != b or b == float('inf') or b == float('-inf'):
            raise TypeError("b must be an integer")
        b = int(b)
    return a + b
