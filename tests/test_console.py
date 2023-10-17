import unittest
import sys
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment and create an instance of the HBNBCommand
        class.
        """
        self.console = HBNBCommand()
        self.console.do_create("User")
        self.capture = StringIO()
        sys.stdout = self.capture

    def tearDown(self):
        """
        Reset the environment and restore the original sys.stdout.
        """
        sys.stdout = sys.__stdout__

    def test_create(self):
        """
        Test the 'create' command.
        """
        self.console.do_create("State")
        expected_output = "[State] ("
        self.assertIn(expected_output, self.capture.getvalue())

    def test_show(self):
        """
        Test the 'show' command.
        """
        # Valid show
        self.console.do_show("User 1")
        expected_output = "[User] (1)"
        self.assertIn(expected_output, self.capture.getvalue())

        # Invalid show
        self.console.do_show("User 12345")
        expected_output = "** no instance found **"
        self.assertIn(expected_output, self.capture.getvalue())

    def test_destroy(self):
        """
        Test the 'destroy' command.
        """
        # Valid destroy
        self.console.do_destroy("User 1")
        self.assertEqual("", self.capture.getvalue())

        # Invalid destroy
        self.console.do_destroy("User 12345")
        expected_output = "** no instance found **"
        self.assertIn(expected_output, self.capture.getvalue())

    def test_all(self):
        """
        Test the 'all' command.
        """
        self.console.do_all("User")
        expected_output = "[User] (1)"
        self.assertIn(expected_output, self.capture.getvalue())

    def test_count(self):
        """
        Test the 'count' command.
        """
        self.console.do_count("User")
        self.assertIn("1", self.capture.getvalue())

    def test_update(self):
        """
        Test the 'update' command.
        """
        # Valid update
        self.console.do_update("User 1 name John")
        self.assertEqual("", self.capture.getvalue())
        # Invalid update
        self.console.do_update("User 12345 name John")
        expected_output = "** no instance found **"
        self.assertIn(expected_output, self.capture.getvalue())


if __name__ == '__main__':
    unittest.main()
