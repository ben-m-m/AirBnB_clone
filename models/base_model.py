#!/usr/bin/python3
""" Base model class """

from uuid import uuid4
import datetime
from engine import storage


class BaseModel:
    """ Base model class """

    def __init__(self, *args, **kwargs):
        """construct a BaseModel
        Args:
            args (tuple): unused
            kwargs (dict): key/value pairs of attributes

        attributes:
            id (str): unique id generated
            created_at (datetime): time of creation
            updated_at (datetime): time of last update

        description:
            if kwargs is not empty, the instance is created from a
            dictionary of keys/values
            otherwise, the instance is created with a unique id and
            the current datetime - timestamped, and added to storage        
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """returns a string representation of the instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
