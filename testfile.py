import unittest
from main import HelloFunction

class MyTestCase(unittest.TestCase):
    def test_something(self):
        value = HelloFunction().helloword()
        self.assertEqual('hello world', value)


if __name__ == '__main__':
    unittest.main()
