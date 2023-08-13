#!/usr/bin/python3
"""
Module for testing the Review class
"""

import unittest
from models.engine.file_storage import FileStorage
from models.review import Review


class testReview(unittest.TestCase):
    """
    Defines the test methods to test the Review class
    """

    def test_review_created(self):
        """
        Tests if a Review class instance is created
        """

        self.assertTrue(Review())

    def test_review_attributes(self):
        """
        Test the attributes in the Review class instance
        """

        review_1 = Review()

        self.assertTrue(hasattr(review_1, "text"))
        self.assertTrue(hasattr(review_1, "id"))
        self.assertTrue(hasattr(review_1, "created_at"))
        self.assertTrue(hasattr(review_1, "updated_at"))
        self.assertTrue(hasattr(review_1, "place_id"))
        self.assertTrue(hasattr(review_1, "user_id"))

    def test_review_id_type(self):
        """
        Test that the id of object is a string
        """

        review_1 = Review()
        self.assertIsInstance(review_1.id, str)

    def test_review_id_values(self):
        """
        Check the object id values are unique between objects
        """

        review_1 = Review()
        review_2 = Review()
        self.assertIsNotNone(review_1.id)
        self.assertIsNotNone(review_2.id)
        self.assertNotEqual(review_1.id, review_2.id)

    def test_review_class_doc(self):
        """
        test documentation for the class is done
        """

        self.assertGreater(len(Review.__doc__), 3)
        self.assertGreater(len(Review.__init__.__doc__), 3)


if __name__ == "__main__":
    unittest.main()
