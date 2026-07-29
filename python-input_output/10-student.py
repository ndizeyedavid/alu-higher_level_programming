#!/usr/bin/python3
"""Defines a Student class with filtered to_json"""


class Student:
    """A student with first_name, last_name, and age"""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dict representation filtered by attrs list"""
        if isinstance(attrs, list) and all(type(a) is str for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
