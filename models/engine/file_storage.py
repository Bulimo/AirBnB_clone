#!/usr/bin/python3
"""
Defines class FileStorage
Serializes instances to a JSON file and deserializes JSON file to instances
"""

import json
import os
from datetime import datetime

class FileStorage:
    """
    Class to perform Serialization and Deserialization to JSON files

    Attributes:
        __file_path
        __objects
    Methods:
        all()
        new()
        save()
        reload()
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Method to ectract the stored objects

        Returns:
            Attribute __objects; the dictionary of all stored objects
        """
        return self.__objects

    def new(self, obj):
        """
        Store created objects into the sictioanry

        Args:
            obj: object class type to be stored
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serialize the __objects to the JSON file in path __file_path

        __objects dictionary contains instances of custom classes.
        We cannot use directly json.dump().
        We have to call the to_dict() method on each object to
        convert it into a dictionary representation
        before serializing it using json.dump().
        """

        serial_objects = {}

        for k, v in self.__objects.items():
            serial_objects[k] = v.to_dict()

        with open(self.__file_path, mode='w', encoding="utf-8") as f:
            json.dump(serial_objects, f)

    def classes(self):
        """_summary_
        """

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        return classes

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise,
        do nothing. If the file doesn’t exist, no exception should be raised)
        """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]]
                        (**v) for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict

    def attributes(self):
            """Returns the valid attributes and their types for classname."""
            attributes = {
                "BaseModel":
                        {"id": str,
                        "created_at": datetime.datetime,
                        "updated_at": datetime.datetime},
                "User":
                        {"email": str,
                        "password": str,
                        "first_name": str,
                        "last_name": str},
                "State":
                        {"name": str},
                "City":
                        {"state_id": str,
                        "name": str},
                "Amenity":
                        {"name": str},
                "Place":
                        {"city_id": str,
                        "user_id": str,
                        "name": str,
                        "description": str,
                        "number_rooms": int,
                        "number_bathrooms": int,
                        "max_guest": int,
                        "price_by_night": int,
                        "latitude": float,
                        "longitude": float,
                        "amenity_ids": list},
                "Review":
                        {"place_id": str,
                        "user_id": str,
                        "text": str}
                        }
            return attributes
