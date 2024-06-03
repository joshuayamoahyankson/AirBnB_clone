#!/usr/bin/python3
"""Module for file storage"""
import datetime
import json
import os


class FileStorage:
    """A class for data storage, retrieving and operations"""
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """A method that returns dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """A method that sets in obj"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """A method that serializes __objects to the JSON file"""
        serial = json.dumps(FileStorage.__objects)
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()},
                file
            )

    def reload(self):
        """A method that deserializes the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(
                FileStorage.__file_path, "r", encoding="utf-8") as des_file:
                data = json.load(des_file)
                FileStorage.__objects = data
        else:
            print()

    @staticmethod
    def classes():
        """A method that returns classes in dictionary format"""
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review
        return {
                    "BaseModel": BaseModel,
                    "User": User,
                    "City": City,
                    "Place": Place,
                    "Amenity": Amenity,
                    "State": State,
                    "Review": Review
                }
