#!/usr/bin/python3
"""
Defines test module for BaseModel class
"""
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """
    Test class for BaseModel class module
    """
    def test_obj_created(self):
        """
        Test if object is created
        """

        self.assertTrue(BaseModel())

    def test_attributes(self):
        """
        Confirm attributes in the object
        """

        base1 = BaseModel()
        self.assertTrue(hasattr(base1, "id"))
        self.assertTrue(hasattr(base1, "created_at"))
        self.assertTrue(hasattr(base1, "updated_at"))

    def test_id_type(self):
        """
        Test that the id of object is a string
        """

        base1 = BaseModel()
        self.assertIsInstance(base1.id, str)

    def test_id_values(self):
        """
        Check the object id values are unique between objects
        """

        base1 = BaseModel()
        base2 = BaseModel()
        self.assertIsNotNone(base1.id)
        self.assertIsNotNone(base2.id)
        self.assertNotEqual(base1.id, base2.id)

    def test_class_doc(self):
        """
        test documentation for the class is done
        """

        doc = BaseModel.__doc__
        self.assertGreater(len(doc), 3)

    def test_function_doc(self):
        """
        test documentation for functions in class
        """
        self.assertGreater(len(BaseModel.__init__.__doc__), 3)
        self.assertGreater(len(BaseModel.save.__doc__), 3)
        self.assertGreater(len(BaseModel.to_dict.__doc__), 3)
