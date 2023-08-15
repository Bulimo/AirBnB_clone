#!/usr/bin/python3
"""
Module to test the serialization and deserialization module
and File_storage_class
"""

import json
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """
    Test the file storage Module
    """

    def setUp(self):
        """
        Setup the class before any test
        Remove the JSON file before running any tests
        """

        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """
        Remove the JSON file after every test
        """

        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_private_attr(self):
        """
        Test that private attributes for class FileStorage are
        not accessible
        """

        self.assertFalse(hasattr(FileStorage, "__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertFalse(hasattr(FileStorage, "__objects"))

    def test_object_created(self):
        """
        Test that an instance of FileStorage object is created
        """

        file_obj = FileStorage()
        self.assertTrue(file_obj)
        self.assertIsInstance(file_obj.all(), dict)

    def test_save_new_method(self):
        """
        Test the methods save and new
        """

        base_obj = BaseModel()
        file_obj = FileStorage()
        file_obj.new(base_obj)
        objs = file_obj.all()
        self.assertIn(base_obj, objs.values())

    def test_reload(self):
        """
        Test that the reload method works
        """

        base_obj = BaseModel()
        file_obj = FileStorage()
        file_obj.new(base_obj)
        file_obj.save()

        new_file = FileStorage()
        new_file.reload()
        objs = new_file.all()
        self.assertTrue(type(objs.values()), BaseModel)

    def test_no_file(self):
        """
        Test that no exception is raised if no file is found
        """

        file_obj = FileStorage()
        try:
            file_obj.reload()
        except FileNotFoundError:
            self.fail("raised FileNotFoundError")

    def test_with_base_model(self):
        """
        Test that the FileStorage correctly intergrates with BaseModel
        """

        base_obj = BaseModel()
        file_obj = FileStorage()
        base_obj.save()

        objs = file_obj.all()
        self.assertIn(base_obj, objs.values())

    def test_all(self):
        """
        Test the all method
        """
        obj = BaseModel()
        file_obj = FileStorage()
        objects = file_obj.all()
        # check that it is a dictionary
        self.assertIsInstance(objects, dict)
        # check that it has the correct key and value
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, objects)
        self.assertEqual(objects[key], obj)

    def test_save(self):
        """
        Test that the save method
        """
        # create a new BaseModel instance and add it to __objects
        obj = BaseModel()
        file_obj = FileStorage()
        file_obj.new(obj)
        file_obj.save()
        self.assertTrue(os.path.exists("file.json"))
        # open the file and load it as a dictionary
        with open("file.json", "r") as f:
            dict_objects = json.load(f)
            # check that it is a dictionary
            self.assertIsInstance(dict_objects, dict)
            # check that it has the correct key and value
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.assertIn(key, dict_objects)
            self.assertEqual(dict_objects[key], obj.to_dict())

    def test_reload_from_empty(self):
        """
        Tests reload from empty file
        """
        file_obj = FileStorage()
        try:
            os.remove("file.json")
        except Exception:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(file_obj.reload(), None)


if __name__ == "__main__":
    unittest.main()
