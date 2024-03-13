#!/usr/bin/env python3
"""
This script defines the Amenity class, which inherits from
the BaseModel class.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity or feature available in a place.

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""
