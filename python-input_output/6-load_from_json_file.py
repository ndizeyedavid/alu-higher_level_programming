#!/usr/bin/python3
"""Creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """Returns Python object from JSON file filename"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
