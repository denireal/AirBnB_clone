#!/usr/bin/env python3
"""
This script defines a FileStorage class responsible for managing objects and
their storage in a JSON file.
"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class FileStorage:
    """
    This class manages the serialization and deserialization of instances into
    JSON format and stores them in a file.

    Attributes:
        __file_path: string - path to the JSON file
        __objects: dictionary - empty but will store objects by <class name>.id
    """

    # File path to store JSON data
    __file_path = "file.json"
    # Dictionary to store objects
    __objects = {}

    def all(self):
        """Returns the dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the __objects dictionary"""
        class_name = type(obj).__name__
        obj_id = obj.id
        key = f"{class_name}.{obj_id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON and saves to the file"""
        new_obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            new_obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_obj_dict, f)

    def reload(self):
        """Deserializes JSON file to recreate objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                objects_loaded = json.load(f)

                new_obj_dict = {}
                for key, dict_obj in objects_loaded.items():
                    class_name = key.split(".")[0]
                    obj = eval(class_name)(**dict_obj)
                    new_obj_dict[key] = obj
                FileStorage.__objects = new_obj_dict
        except FileNotFoundError:
            pass

    def delete(self, obj):
        """Deletes an object from __objects"""
        class_name = type(obj).__name__
        obj_id = obj.id
        key = f"{class_name}.{obj_id}"

        if key in FileStorage.__objects:
            del FileStorage.__objects[key]
            self.save()
            return True

        return False
