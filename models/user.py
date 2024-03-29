#!/usr/bin/env python3
"""
This script contains a class that inherits from the BaseModel class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class definition.

    Attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
