#!/usr/bin/python3
"""Defines a Student class"""


class Student:
    """A student with first_name, last_name, and age"""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary representation of a Student instance"""
        return self.__dict__
