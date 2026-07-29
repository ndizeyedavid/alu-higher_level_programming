#!/usr/bin/python3
"""Unittests for the Square class."""
import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInit(unittest.TestCase):
    """Tests for Square instantiation."""

    def test_is_rectangle_instance(self):
        s = Square(5)
        self.assertIsInstance(s, Rectangle)

    def test_width_equals_height(self):
        s = Square(5)
        self.assertEqual(s.width, s.height)

    def test_all_args(self):
        s = Square(5, 1, 2, 99)
        expected = (5, 5, 1, 2, 99)
        self.assertEqual((s.width, s.height, s.x, s.y, s.id), expected)

    def test_default_x_y(self):
        s = Square(5)
        self.assertEqual((s.x, s.y), (0, 0))

    def test_ctor_size_string(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_ctor_x_string(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_ctor_y_string(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_ctor_size_negative(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_ctor_x_negative(self):
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_ctor_y_negative(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_ctor_size_zero(self):
        with self.assertRaises(ValueError):
            Square(0)


class TestSquareSize(unittest.TestCase):
    """Tests for Square's size property."""

    def test_size_getter(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual((s.width, s.height), (10, 10))

    def test_size_setter_invalid_type(self):
        s = Square(5)
        with self.assertRaises(TypeError) as cm:
            s.size = "9"
        self.assertEqual(str(cm.exception), "width must be an integer")

    def test_size_setter_invalid_value(self):
        s = Square(5)
        with self.assertRaises(ValueError) as cm:
            s.size = -1
        self.assertEqual(str(cm.exception), "width must be > 0")


class TestSquareStr(unittest.TestCase):
    """Tests for Square.__str__."""

    def test_str(self):
        s = Square(3, 1, 3, 5)
        self.assertEqual(str(s), "[Square] (5) 1/3 - 3")


class TestSquareArea(unittest.TestCase):
    """Tests for Square.area (inherited from Rectangle)."""

    def test_area(self):
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(2, 2).area(), 4)


class TestSquareUpdate(unittest.TestCase):
    """Tests for Square.update."""

    def test_update_args(self):
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual((s.id, s.size, s.x, s.y), (1, 2, 3, 4))

    def test_update_partial_args(self):
        s = Square(5)
        s.update(10)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 5)

    def test_update_kwargs(self):
        s = Square(5)
        s.update(size=7, y=1)
        self.assertEqual((s.size, s.y), (7, 1))

    def test_update_kwargs_id(self):
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual((s.id, s.size, s.y), (89, 7, 1))


class TestSquareToDictionary(unittest.TestCase):
    """Tests for Square.to_dictionary."""

    def test_keys(self):
        s = Square(10, 2, 1)
        d = s.to_dictionary()
        self.assertEqual(set(d.keys()), {"id", "size", "x", "y"})

    def test_values(self):
        s = Square(10, 2, 1, 5)
        d = s.to_dictionary()
        self.assertEqual(d, {"id": 5, "size": 10, "x": 2, "y": 1})

    def test_type(self):
        self.assertIsInstance(Square(1).to_dictionary(), dict)


if __name__ == "__main__":
    unittest.main()
