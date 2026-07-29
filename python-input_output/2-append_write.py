#!/usr/bin/python3
"""Appends a string at the end of a text file (UTF8)"""


def append_write(filename="", text=""):
    """Appends text to filename and returns number of characters added"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
