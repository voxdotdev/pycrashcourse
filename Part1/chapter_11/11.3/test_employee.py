import unittest
from employee import Employee

class TestEmployeeRaise(unittest.TestCase):
    """Test for the Employee class."""

    def setUp(self):
        """Make an employee to use in tests."""
        self.someone = Employee('john', 'smith', 65_000)

    def test_give_default_raise(self):
        """Test that default raise works correctly."""
        self.someone.give_raise()
        self.assertEqual(self.someone.salary, 70000)

    def test_give_custom_raise(self):
        """Test that custom raise works correctly."""
        self.someone.give_raise(10000)
        self.assertEqual(self.someone.salary, 75000)

if __name__ == '__main__':
    unittest.main()

