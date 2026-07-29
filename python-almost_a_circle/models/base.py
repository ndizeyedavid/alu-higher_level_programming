#!/usr/bin/python3
"""Module that defines the Base class for all other classes."""
import json


class Base:
    """Base class that manages id attribute for all future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance with a unique id.

        Args:
            id: integer id value, auto-assigned if None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries: list of dictionaries

        Returns:
            str: JSON string, or "[]" if None/empty
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of list_objs to a file.

        Args:
            list_objs: list of Base instances
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]
            ))

    @staticmethod
    def from_json_string(json_string):
        """Returns list from JSON string representation.

        Args:
            json_string: string representing a list of dictionaries

        Returns:
            list: list of dictionaries, or empty list if None/empty
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Args:
            **dictionary: dictionary of attribute values

        Returns:
            Base: instance with attributes set via update
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances loaded from a JSON file.

        Returns:
            list: instances read from file, empty list if file doesn't exist
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                list_dicts = cls.from_json_string(f.read())
            return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
