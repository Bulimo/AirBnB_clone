#!/usr/bin/python3
"""
Module for testing the City class
"""

import unittest
from models.engine.file_storage import FileStorage
from models.city import City


class testCity(unittest.TestCase):
    """
    Defines the test methods to test the City class
    """

    def test_city_created(self):
        """
        Tests if a City class instance is created
        """

        self.assertTrue(City())

    def test_city_attributes(self):
        """
        Test the attributes in the City class instance
        """

        city_1 = City()

        self.assertTrue(hasattr(city_1, "name"))
        self.assertTrue(hasattr(city_1, "id"))
        self.assertTrue(hasattr(city_1, "state_id"))
        self.assertTrue(hasattr(city_1, "created_at"))
        self.assertTrue(hasattr(city_1, "updated_at"))

    def test_city_id_type(self):
        """
        Test that the id of object is a string
        """

        city_1 = City()
        self.assertIsInstance(city_1.id, str)

    def test_city_id_values(self):
        """
        Check the object id values are unique between objects
        """

        city_1 = City()
        city_2 = City()
        self.assertIsNotNone(city_1.id)
        self.assertIsNotNone(city_2.id)
        self.assertNotEqual(city_1.id, city_2.id)

    def test_city_class_doc(self):
        """
        test documentation for the class is done
        """

        doc = City.__doc__
        self.assertGreater(len(doc), 3)

    def test_city_name(self):
        """
        Test that the name of City instance can be updated
        """

        city_1 = City()
        self.assertIsInstance(city_1.name, str)
        self.assertEqual(city_1.name, "")
        city_1.name = "Nairobi"
        self.assertTrue(city_1.name, "Nairobi")


if __name__ == "__main__":
    unittest.main()
