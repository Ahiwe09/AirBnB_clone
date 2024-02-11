#!/usr/bin/python3
"""
This module houses a class named `BaseModel`,
which serves as the foundational structure
for other classes within the AirBnB Clone project.
"""
from uuid import uuid4
import datetime

class BaseModel:
    """ this is the Base class for other class"""

    def __init__(self, *args, **kwargs):
        """
        initialize a value
        """

        if kwargs != {}:
            for key in kwargs.keys():
                if key == "__class__":
                    continue
                if key =="updated_at" or key == "created_at":
                    kwargs[key] = datetime.datetime.fromisoformat(kwargs[key])
                setattr(self, key, kwargs[key])
            return
        self.id = str(uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()

    def __str__(self):
        """
        Return the print/str representation of the BaseModel instance.
        """

        return("[{}] ({}) {}".format(type(self).__name__,self.id, self.__dict__))

    def save(self):

        """updated_at with the current datetime.
        """

        self.updated_at = datetime.datetime.today()

    def to_dict(self):
        """Return dictionary of the Basemodel
        """

        updated_at_str = self.__dict__["updated_at"].isoformat()
        created_at_str = self.__dict__["created_at"].isoformat()
        obj_dict = self.__dict__.copy()
        obj_dict["updated_at"] = updated_at_str
        obj_dict["created_at"] = created_at_str
        obj_dict["__class__"] = type(self).__name__
        return obj_dict
