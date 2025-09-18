import unittest
from io import StringIO
import sys

class TestHelloWorld(unittest.TestCase):
    def test_hello_output(self):
        from TestFiles import hello
        captured_output = StringIO()
        sys.stdout = captured_output
        hello.print("Hello, world!")
        sys.stdout = sys.__stdout__
        self.assertIn("Hello, world!", captured_output.getvalue())

if __name__ == "__main__":
    unittest.main()
