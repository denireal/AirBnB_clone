#!/usr/bin/env python3
"""
BaseModel Class containing modules of the project.
"""
import models
import uuid
from datetime import datetime

time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Specifies the structure or blueprint for the subclasses.

    Attributes:
        id: string - Assign a UUID to an object upon its creation.
        creation_date: datetime - Assign the current datetime to an object
                    when it is created.
        last_updated: datetime - Assigns the current datetime to an object
                    when it is created and updates it each time the object
                    is modified.
    """

    def __init__(self, *args, **kwargs):
        """A method within a class or constructor function used to create
        new instances of an object."""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "creation_date" or key == "last_updated":
                        self.__dict__[key] = datetime.strptime(
                            value, time_format)
                    else:
                        self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.creation_date = datetime.now()
            self.last_updated = self.creation_date
            models.storage.new(self)

    def __str__(self):
        """String representation of object"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updating last_updated with the current datetime and
        save modelobject"""
        self.last_updated = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary that has been modified to include all
        attributes of an object"""
        new_obj_dict = self.__dict__.copy()
        new_obj_dict["__class__"] = type(self).__name__
        new_obj_dict["creation_date"] = self.creation_date.strftime(time_format)
        new_obj_dict["last_updated"] = self.last_updated.strftime(time_format)
        return new_obj_dict
