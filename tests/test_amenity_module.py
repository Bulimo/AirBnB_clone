#!/usr/bin/python3
"""
Module for testing the Amenity class
"""

import unittest
from models.engine.file_storage import FileStorage
from models.amenity import Amenity


class testAmenity(unittest.TestCase):
    """
    Defines the test methods to test the Amenity class
    """

    def test_amenity_created(self):
        """
        Tests if a Amenity class instance is created
        """

        self.assertTrue(Amenity())

    def test_attributes(self):
        """
        Test the attributes in the Amenity class instance
        """

        amenity_1 = Amenity()

        self.assertTrue(hasattr(amenity_1, "name"))
        self.assertTrue(hasattr(amenity_1, "id"))
        self.assertTrue(hasattr(amenity_1, "created_at"))
        self.assertTrue(hasattr(amenity_1, "updated_at"))

    def test_amenity_id_type(self):
        """
        Test that the id of object is a string
        """

        amenity_1 = Amenity()
        self.assertIsInstance(amenity_1.id, str)

    def test_amenity_id_values(self):
        """
        Check the object id values are unique between objects
        """

        amenity_1 = Amenity()
        amenity_2 = Amenity()
        self.assertIsNotNone(amenity_1.id)
        self.assertIsNotNone(amenity_2.id)
        self.assertNotEqual(amenity_1.id, amenity_2.id)

    def test_class_doc(self):
        """
        test documentation for the class is done
        """

        doc = Amenity.__doc__
        self.assertGreater(len(doc), 3)

    def test_amenity_name(self):
        """
        Test that the name of Amenity instance can be updated
        """

        amenity_1 = Amenity()
        self.assertIsInstance(amenity_1.name, str)
        self.assertEqual(amenity_1.name, "")
        amenity_1.name = "bathroom"
        self.assertTrue(amenity_1.name, "bathroom")


if __name__ == "__main__":
    unittest.main()
