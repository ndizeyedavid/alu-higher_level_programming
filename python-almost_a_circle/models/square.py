#!/usr/bin/python3
"""Module that defines the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance.

        Args:
            size: square side length
            x: x position (default 0)
            y: y position (default 0)
            id: instance id (auto-assigned if None)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get square size."""
        return self.width

    @size.setter
    def size(self, value):
        """Set square size (updates both width and height)."""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns string representation of square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """Assigns arguments to attributes.

        Args:
            *args: no-keyword arguments (id, size, x, y)
            **kwargs: key-worded arguments
        """
        if args and len(args) > 0:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionary representation of square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
