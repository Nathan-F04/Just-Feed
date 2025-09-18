"""Test module for hello functionality."""
import unittest
from io import StringIO
import sys
from TestFiles import hello

class TestHelloWorld(unittest.TestCase):
    """Test class for hello world functionality."""
    
    def test_hello_output(self):
        """Test hello output message."""
        captured_output = StringIO()
        sys.stdout = captured_output
        hello.print_message("Hello, world!")
        sys.stdout = sys.__stdout__
        self.assertIn("Hello, world!", captured_output.getvalue())

if __name__ == "__main__":
    unittest.main()
