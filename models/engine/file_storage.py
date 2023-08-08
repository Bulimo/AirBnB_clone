#!/usr/bin/python3
"""
Defines class FileStorage
Serializes instances to a JSON file and deserializes JSON file to instances
"""

import json
import os


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
        return FileStorage.__objects

    def new(self, obj):
        """
        Store created objects into the sictioanry

        Args:
            obj: object class type to be stored
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

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

        for k, v in FileStorage.__objects.items():
            serial_objects[k] = v.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="utf-8") as f:
            json.dump(serial_objects, f)

    def reload(self):
        """
        Deserialize the JSON file to __objects.
        If __file_path does not exit, do nothing.
        """

        from models.base_model import BaseModel
        classes = {"BaseModel": BaseModel}

        try:
            with open(FileStorage.__file_path, mode='r') as file:
                obj_data = json.load(file)

                if len(obj_data) > 0:
                    for val in obj_data.values():
                        class_name = val["__class__"]
                        if class_name in classes.keys():
                            class_obj = classes[class_name]
                            self.new(class_obj(**val))

        except FileNotFoundError:
            pass
