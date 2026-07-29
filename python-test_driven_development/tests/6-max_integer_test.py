#!/usr/bin/python3
"""Unittest for max_integer([..])."""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Test with a list of integers in ascending order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with a list of integers in random order."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test with max at the beginning."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_at_end(self):
        """Test with max at the end."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_one_element(self):
        """Test with a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with all negative numbers."""
        self.assertEqual(max_integer([-5, -3, -1, -10]), -1)

    def test_mixed_numbers(self):
        """Test with a mix of positive and negative numbers."""
        self.assertEqual(max_integer([-10, 0, 5, -3, 8]), 8)

    def test_duplicates(self):
        """Test with duplicate max values."""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_large_numbers(self):
        """Test with large integers."""
        self.assertEqual(max_integer([1000000, 999999, 500000]), 1000000)

    def test_floats(self):
        """Test with float values."""
        self.assertEqual(max_integer([1.5, 2.7, 3.2, 0.8]), 3.2)

    def test_mixed_int_float(self):
        """Test with mixed int and float values."""
        self.assertEqual(max_integer([1, 2.5, 3, 0.5]), 3)

    def test_single_negative(self):
        """Test with a single negative number."""
        self.assertEqual(max_integer([-1]), -1)

    def test_all_same(self):
        """Test with all identical elements."""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_list_with_zero(self):
        """Test with zero in the list."""
        self.assertEqual(max_integer([0, -1, -5]), 0)


if __name__ == '__main__':
    unittest.main()
