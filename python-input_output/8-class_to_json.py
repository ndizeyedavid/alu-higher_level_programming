#!/usr/bin/python3
"""Returns dict description for JSON serialization of an object"""


def class_to_json(obj):
    """Returns dictionary description of obj for JSON serialization"""
    return obj.__dict__
