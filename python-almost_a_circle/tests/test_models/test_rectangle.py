#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleInstantiation(unittest.TestCase):
    """Tests for Rectangle instantiation."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def test_rectangle_is_base(self):
        """Test Rectangle inherits from Base."""
        self.assertIsInstance(Rectangle(1, 1), Base)

    def test_no_args(self):
        """Test Rectangle() raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """Test Rectangle(1) raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        """Test Rectangle(1, 2) creates instance."""
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_all_args(self):
        """Test Rectangle(1, 2, 3, 4, 5)."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_id_auto_assign(self):
        """Test auto id assignment."""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2)
        self.assertEqual(r1.id, r2.id - 1)


class TestRectangleWidthValidation(unittest.TestCase):
    """Tests for width validation."""

    def test_width_string(self):
        """Test width as string raises TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("hello", 1)

    def test_width_float(self):
        """Test width as float raises TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.5, 1)

    def test_width_zero(self):
        """Test width 0 raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1)

    def test_width_negative(self):
        """Test negative width raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 1)


class TestRectangleHeightValidation(unittest.TestCase):
    """Tests for height validation."""

    def test_height_string(self):
        """Test height as string raises TypeError."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "hello")

    def test_height_float(self):
        """Test height as float raises TypeError."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 1.5)

    def test_height_zero(self):
        """Test height 0 raises ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    def test_height_negative(self):
        """Test negative height raises ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)


class TestRectangleXValidation(unittest.TestCase):
    """Tests for x validation."""

    def test_x_string(self):
        """Test x as string raises TypeError."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "hello")

    def test_x_negative(self):
        """Test negative x raises ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -1)


class TestRectangleYValidation(unittest.TestCase):
    """Tests for y validation."""

    def test_y_string(self):
        """Test y as string raises TypeError."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 0, "hello")

    def test_y_negative(self):
        """Test negative y raises ValueError."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 0, -1)


class TestRectangleArea(unittest.TestCase):
    """Tests for area method."""

    def test_area_small(self):
        """Test area of small rectangle."""
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_area_large(self):
        """Test area of large rectangle."""
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_area_square(self):
        """Test area of square-like rectangle."""
        self.assertEqual(Rectangle(5, 5).area(), 25)


class TestRectangleDisplay(unittest.TestCase):
    """Tests for display method."""

    def test_display_no_offset(self):
        """Test display without x, y offset."""
        import io
        import sys
        r = Rectangle(2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_display_with_y(self):
        """Test display with y offset."""
        import io
        import sys
        r = Rectangle(2, 2, 0, 1)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n##\n##\n")

    def test_display_with_x(self):
        """Test display with x offset."""
        import io
        import sys
        r = Rectangle(2, 2, 1)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        expected = " ##\n ##\n"
        self.assertEqual(captured.getvalue(), expected)


class TestRectangleStr(unittest.TestCase):
    """Tests for __str__ method."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def test_str_method(self):
        """Test string representation of rectangle."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_defaults(self):
        """Test string with default x, y."""
        r = Rectangle(5, 5, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 1/0 - 5/5")


class TestRectangleUpdate(unittest.TestCase):
    """Tests for update method."""

    def test_update_args_id(self):
        """Test update with one arg (id)."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_args_width(self):
        """Test update with two args (id, width)."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual(r.width, 2)

    def test_update_args_height(self):
        """Test update with three args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual(r.height, 3)

    def test_update_args_x(self):
        """Test update with four args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual(r.x, 4)

    def test_update_args_y(self):
        """Test update with five args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.y, 5)

    def test_update_kwargs(self):
        """Test update with kwargs."""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(r.height, 1)

    def test_update_kwargs_multiple(self):
        """Test update with multiple kwargs."""
        r = Rectangle(10, 10, 10, 10)
        r.update(width=1, x=2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.x, 2)

    def test_update_args_overrides_kwargs(self):
        """Test args override kwargs."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, width=1)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)


class TestRectangleToDictionary(unittest.TestCase):
    """Tests for to_dictionary method."""

    def test_to_dictionary(self):
        """Test dictionary representation."""
        r = Rectangle(10, 2, 1, 9)
        d = r.to_dictionary()
        expected = {"id": r.id, "x": 1, "y": 9, "width": 10, "height": 2}
        self.assertEqual(d, expected)

    def test_to_dictionary_type(self):
        """Test to_dictionary returns dict."""
        r = Rectangle(1, 1)
        self.assertIsInstance(r.to_dictionary(), dict)

    def test_to_dictionary_update(self):
        """Test update(**to_dictionary()) creates same rectangle."""
        r1 = Rectangle(10, 2, 1, 9)
        d = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**d)
        self.assertEqual(str(r1), str(r2))


if __name__ == "__main__":
    unittest.main()
