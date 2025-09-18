"""Hello module."""
# hello.py
print("Hello, world!")

def print(message):
    """Print a message."""
    __builtins__['print'](message)

# sum_example.py
def add(a, b):
    """Add two numbers."""
    return a + b

if __name__ == "__main__":
    print("Sum of 2 and 3 is:", add(2, 3))
