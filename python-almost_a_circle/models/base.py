#!/usr/bin/python3
"""Defines the Base class."""
import json
import csv


class Base:
    """Base class that manages the id attribute for all other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): the identity of the new instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dicts.

        Args:
            list_dictionaries (list): a list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): a list of instances that inherit from Base.
        """
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            list_objs = []

        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string.

        Args:
            json_string (str): a JSON string representing a list of dicts.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set.

        Args:
            dictionary (dict): key/value pairs of attributes to set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from <Class name>.json."""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as f:
                list_dicts = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []

        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV string representation of list_objs to a file.

        Args:
            list_objs (list): a list of instances that inherit from Base.
        """
        filename = "{}.csv".format(cls.__name__)
        if list_objs is None:
            list_objs = []
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y]
                    )
                else:
                    writer.writerow(
                        [obj.id, obj.size, obj.x, obj.y]
                    )

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances loaded from <Class name>.csv."""
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, "r", newline="") as f:
                reader = csv.reader(f)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        d = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])
                        }
                    else:
                        d = {
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])
                        }
                    instances.append(cls.create(**d))
            return instances
        except FileNotFoundError:
            return []
