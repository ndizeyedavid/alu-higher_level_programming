#!/usr/bin/python3
"""Returns an object (Python data structure) represented by a JSON string"""
import json


def from_json_string(my_str):
    """Returns Python object represented by JSON string my_str"""
    return json.loads(my_str)
