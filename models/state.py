#!/usr/bin/env python3
"""
This script defines the State class, which inherits
from the BaseModel class.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class represents a geographical state.

    Attributes:
        name (str): The name of the state.
    """
    name = ""
