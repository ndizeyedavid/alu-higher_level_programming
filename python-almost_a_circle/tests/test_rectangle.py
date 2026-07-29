#!/usr/bin/python3
"""Unittests for the Rectangle class."""
import unittest
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInit(unittest.TestCase):
    """Tests for Rectangle instantiation."""

    def test_width_height(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)

    def test_default_x_y(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_all_args(self):
        r = Rectangle(10, 2, 1, 3, 12)
        expected = (10, 2, 1, 3, 12)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id), expected)

    def test_is_base_instance(self):
        r = Rectangle(10, 2)
        self.assertIsInstance(r, Base)


class TestRectangleValidation(unittest.TestCase):
    """Tests for Rectangle attribute validation."""

    def test_width_not_int(self):
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, "2")
        self.assertEqual(str(cm.exception), "height must be an integer")

    def test_width_zero(self):
        with self.assertRaises(ValueError) as cm:
            Rectangle(0, 2)
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_width_negative(self):
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError) as cm:
            r.width = -10
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_x_not_int(self):
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError) as cm:
            r.x = {}
        self.assertEqual(str(cm.exception), "x must be an integer")

    def test_y_negative(self):
        with self.assertRaises(ValueError) as cm:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(str(cm.exception), "y must be >= 0")

    def test_ctor_width_string(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_ctor_x_string(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_ctor_y_string(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_ctor_width_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_ctor_height_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_ctor_x_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)


class TestRectangleArea(unittest.TestCase):
    """Tests for Rectangle.area."""

    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)


class TestRectangleDisplay(unittest.TestCase):
    """Tests for Rectangle.display."""

    def test_display_basic(self):
        r = Rectangle(2, 2)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "##\n##\n")

    def test_display_with_offset(self):
        r = Rectangle(3, 2, 1, 0)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), " ###\n ###\n")

    def test_display_with_y_offset(self):
        r = Rectangle(2, 3, 2, 2)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(
                fake_out.getvalue(), "\n\n  ##\n  ##\n  ##\n")


class TestRectangleStr(unittest.TestCase):
    """Tests for Rectangle.__str__."""

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_default_id(self):
        r = Rectangle(5, 5, 1, id=99)
        self.assertEqual(str(r), "[Rectangle] (99) 1/0 - 5/5")


class TestRectangleUpdate(unittest.TestCase):
    """Tests for Rectangle.update."""

    def test_update_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_partial_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 10)

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual((r.x, r.height, r.y, r.width), (1, 2, 3, 4))

    def test_update_args_skips_kwargs(self):
        r = Rectangle(10, 10)
        r.update(5, height=99)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.height, 10)


class TestRectangleToDictionary(unittest.TestCase):
    """Tests for Rectangle.to_dictionary."""

    def test_to_dictionary_keys(self):
        r = Rectangle(10, 2, 1, 9)
        d = r.to_dictionary()
        self.assertEqual(
            set(d.keys()), {"id", "width", "height", "x", "y"})

    def test_to_dictionary_values(self):
        r = Rectangle(10, 2, 1, 9, 5)
        d = r.to_dictionary()
        self.assertEqual(
            d, {"id": 5, "width": 10, "height": 2, "x": 1, "y": 9})

    def test_to_dictionary_type(self):
        r = Rectangle(1, 1)
        self.assertIsInstance(r.to_dictionary(), dict)


if __name__ == "__main__":
    unittest.main()
