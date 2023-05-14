#!/usr/bin/python3
""" File storage class """

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import os.path


class FileStorage:
    """Storage class for objects
    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): objects will be stored
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Init method"""
        pass

    def all(self):
        """Returns the dictionary __objects"""
        self.reload()
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj
        self.save()

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            if os.path.isfile(self.__file_path):
                with open(self.__file_path, "r") as f:
                    for key, value in json.load(f).items():
                        self.__objects[key] = eval(value["__class__"])(**value)
        except FileNotFoundError:
            return
        except json.JSONDecodeError:
            return

    def delete(self, obj=None):
        """Delete obj from __objects if it’s inside"""
        if obj is None:
            return
        if obj in self.__objects:
            del self.__objects[obj]
        self.save()
    
    def update(self, obj, k, v):
        """Update obj in __objects with k : v as attributes"""
        # if obj is None:
        #     return
        if obj in self.__objects:
            setattr(self.__objects[obj], k, eval(v))
        self.save()
