#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
import os
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquareInstantiation(unittest.TestCase):
    """Tests for Square instantiation."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def test_square_is_rectangle(self):
        """Test Square inherits from Rectangle."""
        self.assertIsInstance(Square(1), Rectangle)

    def test_square_is_base(self):
        """Test Square inherits from Base."""
        self.assertIsInstance(Square(1), Base)

    def test_no_args(self):
        """Test Square() raises TypeError."""
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        """Test Square(5) creates instance with correct size."""
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_all_args(self):
        """Test Square(5, 1, 2, 10)."""
        s = Square(5, 1, 2, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 10)


class TestSquareSizeValidation(unittest.TestCase):
    """Tests for size validation."""

    def test_size_string(self):
        """Test size as string raises TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("hello")

    def test_size_zero(self):
        """Test size 0 raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_size_negative(self):
        """Test negative size raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)


class TestSquareXValidation(unittest.TestCase):
    """Tests for x validation on Square."""

    def test_x_string(self):
        """Test x as string raises TypeError."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")

    def test_x_negative(self):
        """Test negative x raises ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)


class TestSquareYValidation(unittest.TestCase):
    """Tests for y validation on Square."""

    def test_y_string(self):
        """Test y as string raises TypeError."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_y_negative(self):
        """Test negative y raises ValueError."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)


class TestSquareStr(unittest.TestCase):
    """Tests for __str__ method."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def test_str_method(self):
        """Test string representation of square."""
        s = Square(5)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    def test_str_with_attrs(self):
        """Test string with x, y, id."""
        s = Square(3, 1, 3)
        self.assertEqual(str(s), "[Square] (1) 1/3 - 3")


class TestSquareUpdate(unittest.TestCase):
    """Tests for update method."""

    def test_update_args_id(self):
        """Test update with one arg (id)."""
        s = Square(5)
        s.update(10)
        self.assertEqual(s.id, 10)

    def test_update_args_size(self):
        """Test update with two args (id, size)."""
        s = Square(5)
        s.update(1, 2)
        self.assertEqual(s.size, 2)

    def test_update_args_x(self):
        """Test update with three args."""
        s = Square(5)
        s.update(1, 2, 3)
        self.assertEqual(s.x, 3)

    def test_update_args_y(self):
        """Test update with four args."""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        """Test update with kwargs."""
        s = Square(5)
        s.update(size=7, y=1)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.y, 1)

    def test_update_kwargs_id(self):
        """Test update with id kwarg."""
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.y, 1)


class TestSquareToDictionary(unittest.TestCase):
    """Tests for to_dictionary method."""

    def test_to_dictionary(self):
        """Test dictionary representation."""
        s = Square(10, 2, 1)
        d = s.to_dictionary()
        expected = {"id": s.id, "x": 2, "size": 10, "y": 1}
        self.assertEqual(d, expected)

    def test_to_dictionary_type(self):
        """Test to_dictionary returns dict."""
        s = Square(1)
        self.assertIsInstance(s.to_dictionary(), dict)

    def test_to_dictionary_update(self):
        """Test update(**to_dictionary()) creates same square."""
        s1 = Square(10, 2, 1)
        d = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**d)
        self.assertEqual(str(s1), str(s2))


class TestSquareArea(unittest.TestCase):
    """Tests for area method."""

    def test_area(self):
        """Test area of square."""
        self.assertEqual(Square(5).area(), 25)

    def test_area_large(self):
        """Test area of large square."""
        self.assertEqual(Square(10).area(), 100)


class TestSquareDisplay(unittest.TestCase):
    """Tests for display method."""

    def test_display(self):
        """Test display output."""
        import io
        import sys
        s = Square(2)
        captured = io.StringIO()
        sys.stdout = captured
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")


class TestSquareSaveToFile(unittest.TestCase):
    """Tests for Square.save_to_file method."""

    def setUp(self):
        """Remove test file before each test."""
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """Clean up test file."""
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_save_none(self):
        """Test save_to_file(None) writes empty list."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")

    def test_save_empty(self):
        """Test save_to_file([]) writes empty list."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")

    def test_save_one_square(self):
        """Test save_to_file with one square."""
        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertIn("size", content)


class TestSquareLoadFromFile(unittest.TestCase):
    """Tests for Square.load_from_file method."""

    def setUp(self):
        """Remove test file before each test."""
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """Clean up test file."""
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_load_no_file(self):
        """Test load_from_file returns [] when file doesn't exist."""
        result = Square.load_from_file()
        self.assertEqual(result, [])

    def test_load_file_exists(self):
        """Test load_from_file returns correct instances."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        result = Square.load_from_file()
        self.assertEqual(len(result), 2)
        self.assertEqual(str(result[0]), str(s1))
        self.assertEqual(str(result[1]), str(s2))


if __name__ == "__main__":
    unittest.main()
