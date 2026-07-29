#!/usr/bin/python3
"""Module that prints text with 2 new lines after ., ? and :."""


def text_indentation(text):
    """Prints text with 2 new lines after each of the characters ., ? and :.

    Args:
        text: string to process

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for c in text:
        result += c
        if c in ".?:":
            print(result.strip(), end="")
            print("\n\n", end="")
            result = ""
    if result:
        print(result.strip(), end="")
