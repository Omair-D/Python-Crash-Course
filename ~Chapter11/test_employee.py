import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the module employee."""

    def setUp(self):
        """Make an employee to use in tests."""
        self.lebron = Employee('lebron', 'james', 65_000)

    def test_give_default_raise(self):
        """Test that a default raise works correctly."""
        self.lebron.give_raise()
        self.assertEqual(self.lebron.salary, 70000)

    def test_give_custom_raise(self):
        """Test that a custom raise works correctly."""
        self.lebron.give_raise(10000)
        self.assertEqual(self.lebron.salary, 75000)

if __name__ == '__main__':
    unittest.main()