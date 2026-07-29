#!/usr/bin/python3
"""Unit tests for the Base class."""
import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    """Tests for Base class instantiation."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def test_no_id(self):
        """Test Base() auto-assigns id."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_custom_id(self):
        """Test Base(id=5) assigns given id."""
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_custom_id_string(self):
        """Test Base(id="hello") assigns string id."""
        b = Base("hello")
        self.assertEqual(b.id, "hello")

    def test_custom_id_negative(self):
        """Test Base(id=-1) assigns given id."""
        b = Base(-1)
        self.assertEqual(b.id, -1)

    def test_id_after_custom(self):
        """Test auto-id increments after custom id."""
        Base(12)
        b = Base()
        self.assertEqual(b.id, 1)


class TestBaseToJsonString(unittest.TestCase):
    """Tests for Base.to_json_string method."""

    def test_empty_list(self):
        """Test to_json_string([]) returns "[]"."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_none_list(self):
        """Test to_json_string(None) returns "[]"."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_single_dict(self):
        """Test to_json_string with one dict."""
        d = {"id": 1, "width": 10}
        result = Base.to_json_string([d])
        self.assertIn('"id": 1', result)
        self.assertIn('"width": 10', result)

    def test_multiple_dicts(self):
        """Test to_json_string with multiple dicts."""
        d1 = {"id": 1}
        d2 = {"id": 2}
        result = Base.to_json_string([d1, d2])
        self.assertEqual(len(result.split("},")), 2)

    def test_return_type(self):
        """Test to_json_string returns a string."""
        self.assertIsInstance(Base.to_json_string([{"a": 1}]), str)


class TestBaseSaveToFile(unittest.TestCase):
    """Tests for Base.save_to_file method."""

    def setUp(self):
        """Remove test files before each test."""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """Clean up test files."""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_save_rectangles(self):
        """Test save_to_file with rectangles."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertIn("width", content)
        self.assertIn("height", content)

    def test_save_none(self):
        """Test save_to_file with None."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")

    def test_save_empty_list(self):
        """Test save_to_file with empty list."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")


class TestBaseFromJsonString(unittest.TestCase):
    """Tests for Base.from_json_string method."""

    def test_empty_string(self):
        """Test from_json_string("") returns []."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_none_string(self):
        """Test from_json_string(None) returns []."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_valid_string(self):
        """Test from_json_string with valid JSON."""
        s = '[{"id": 1, "width": 10}]'
        result = Base.from_json_string(s)
        self.assertEqual(result, [{"id": 1, "width": 10}])

    def test_return_type(self):
        """Test from_json_string returns a list."""
        result = Base.from_json_string('[{"id": 1}]')
        self.assertIsInstance(result, list)


class TestBaseCreate(unittest.TestCase):
    """Tests for Base.create method."""

    def test_create_rectangle(self):
        """Test create rectangle from dictionary."""
        r1 = Rectangle(3, 5, 1)
        d = r1.to_dictionary()
        r2 = Rectangle.create(**d)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        """Test create square from dictionary."""
        s1 = Square(3, 1, 2)
        d = s1.to_dictionary()
        s2 = Square.create(**d)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)


class TestBaseLoadFromFile(unittest.TestCase):
    """Tests for Base.load_from_file method."""

    def setUp(self):
        """Remove test files before each test."""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """Clean up test files."""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    def test_load_no_file(self):
        """Test load_from_file returns [] when file doesn't exist."""
        result = Rectangle.load_from_file()
        self.assertEqual(result, [])

    def test_load_rectangles(self):
        """Test load_from_file returns correct instances."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        result = Rectangle.load_from_file()
        self.assertEqual(len(result), 2)
        self.assertEqual(str(result[0]), str(r1))
        self.assertEqual(str(result[1]), str(r2))


if __name__ == "__main__":
    unittest.main()
