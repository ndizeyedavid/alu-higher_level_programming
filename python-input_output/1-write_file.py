#!/usr/bin/python3
"""Writes a string to a text file (UTF8) and returns char count"""


def write_file(filename="", text=""):
    """Writes text to filename and returns number of characters written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
