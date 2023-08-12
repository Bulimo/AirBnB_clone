#!/usr/bin/python3
"""
module that defines the Amenity class
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.
    Public class attributes:
        name: string - empty string
    """
    name = ""
