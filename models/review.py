#!/usr/bin/env python3
"""
This script defines the Review class, which inherits from
the BaseModel class.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Reepresents a review associated with a place and a user.

    Attributes:
        place_id (str): The ID of the place being reviewed.
        user_id (str): The ID of the user who wrote the review.
        text (str): The content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
