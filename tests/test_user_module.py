#!/usr/bin/python3
"""
Module for testing the User class
"""

import unittest
from models.engine.file_storage import FileStorage
from models.user import User


class testUser(unittest.TestCase):
    """
    Defines the test methods to test the User class
    """

    def test_user_created(self):
        """
        Tests if a User class instance is created
        """

        self.assertTrue(User())

    def test_attributes(self):
        """
        Test the attributes in the User class instance
        """

        user_1 = User()

        self.assertTrue(hasattr(user_1, "email"))
        self.assertTrue(hasattr(user_1, "password"))
        self.assertTrue(hasattr(user_1, "first_name"))
        self.assertTrue(hasattr(user_1, "last_name"))
        self.assertTrue(hasattr(user_1, "id"))
        self.assertTrue(hasattr(user_1, "created_at"))
        self.assertTrue(hasattr(user_1, "updated_at"))

    def test_user_id_type(self):
        """
        Test that the id of object is a string
        """

        user_1 = User()
        self.assertIsInstance(user_1.id, str)

    def test_user_id_values(self):
        """
        Check the object id values are unique between objects
        """

        user_1 = User()
        user_2 = User()
        self.assertIsNotNone(user_1.id)
        self.assertIsNotNone(user_2.id)
        self.assertNotEqual(user_1.id, user_2.id)

    def test_class_doc(self):
        """
        test documentation for the class is done
        """

        doc = User.__doc__
        self.assertGreater(len(doc), 3)
        self.assertGreater(len(User.__init__.__doc__), 3)


if __name__ == "__main__":
    unittest.main()
