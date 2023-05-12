#!/usr/bin/python3
""" File storage class """

import json


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
        return self.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj
        
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
            with open(self.__file_path, "r") as f:
                new_dict = json.load(f)
                for key, value in new_dict.items():
                    class_name = value["__class__"]
                    self.__objects[key] = eval(class_name + "(**value)")
        except FileNotFoundError:
            pass