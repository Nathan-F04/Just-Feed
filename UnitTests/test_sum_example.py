"""Test module for sum example functionality."""
import unittest
from TestFiles.sum_example import add

class TestSumExample(unittest.TestCase):
    """Test class for sum example functionality."""
    def test_add_positive(self):
        """Test adding positive numbers."""
        self.assertEqual(add(2, 3), 5)

    def test_add_zero(self):
        """Test adding zeros."""
        self.assertEqual(add(0, 0), 0)

    def test_add_negative(self):
        """Test adding negative numbers."""
        self.assertEqual(add(-1, -1), -2)

if __name__ == "__main__":
    unittest.main()
