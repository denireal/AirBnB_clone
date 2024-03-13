#!/usr/bin/env python3
"""
This script defines the City class, which inherits from
the BaseModel class.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class represents a city within a geographical state.

    Attributes:
        state_id (str): The ID of the state to which the city belongs.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
