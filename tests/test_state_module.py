#!/usr/bin/python3
"""
Module for testing the State class
"""

import unittest
from models.engine.file_storage import FileStorage
from models.state import State


class testState(unittest.TestCase):
    """
    Defines the test methods to test the State class
    """

    def test_state_created(self):
        """
        Tests if a State class instance is created
        """

        self.assertTrue(State())

    def test_state_attributes(self):
        """
        Test the attributes in the State class instance
        """

        state_1 = State()

        self.assertTrue(hasattr(state_1, "name"))
        self.assertTrue(hasattr(state_1, "id"))
        self.assertTrue(hasattr(state_1, "created_at"))
        self.assertTrue(hasattr(state_1, "updated_at"))

    def test_state_id_type(self):
        """
        Test that the id of object is a string
        """

        state_1 = State()
        self.assertIsInstance(state_1.id, str)

    def test_state_id_values(self):
        """
        Check the object id values are unique between objects
        """

        state_1 = State()
        state_2 = State()
        self.assertIsNotNone(state_1.id)
        self.assertIsNotNone(state_2.id)
        self.assertNotEqual(state_1.id, state_2.id)

    def test_state_class_doc(self):
        """
        test documentation for the class is done
        """

        self.assertGreater(len(State.__doc__), 3)
        self.assertGreater(len(State.__init__.__doc__), 3)


if __name__ == "__main__":
    unittest.main()
