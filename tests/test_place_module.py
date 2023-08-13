#!/usr/bin/python3
"""
Module for testing the Place class
"""

import unittest
from models.engine.file_storage import FileStorage
from models.place import Place


class testPlace(unittest.TestCase):
    """
    Defines the test methods to test the Place class
    """

    def test_place_created(self):
        """
        Tests if a Place class instance is created
        """

        self.assertTrue(Place())

    def test_place_attributes(self):
        """
        Test the attributes in the Place class instance
        """

        place_1 = Place()

        self.assertTrue(hasattr(place_1, "name"))
        self.assertTrue(hasattr(place_1, "id"))
        self.assertTrue(hasattr(place_1, "created_at"))
        self.assertTrue(hasattr(place_1, "updated_at"))
        self.assertTrue(hasattr(place_1, "city_id"))
        self.assertTrue(hasattr(place_1, "user_id"))
        self.assertTrue(hasattr(place_1, "description"))
        self.assertTrue(hasattr(place_1, "number_rooms"))
        self.assertTrue(hasattr(place_1, "number_bathrooms"))
        self.assertTrue(hasattr(place_1, "max_guest"))
        self.assertTrue(hasattr(place_1, "price_by_night"))
        self.assertTrue(hasattr(place_1, "latitude"))
        self.assertTrue(hasattr(place_1, "longitude"))
        self.assertTrue(hasattr(place_1, "amenity_ids"))

    def test_place_id_type(self):
        """
        Test that the id of object is a string
        """

        place_1 = Place()
        self.assertIsInstance(place_1.id, str)

    def test_place_id_values(self):
        """
        Check the object id values are unique between objects
        """

        place_1 = Place()
        place_2 = Place()
        self.assertIsNotNone(place_1.id)
        self.assertIsNotNone(place_2.id)
        self.assertNotEqual(place_1.id, place_2.id)

    def test_place_class_doc(self):
        """
        test documentation for the class is done
        """

        self.assertGreater(len(Place.__doc__), 3)
        self.assertGreater(len(Place.__init__.__doc__), 3)


if __name__ == "__main__":
    unittest.main()
