#!/usr/bin/python3
"""
module that defines the City class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel.
    Public class attributes:
        state_id: string - empty string (State.id)
        name: string - empty string
    """
    state_id = ""
    name = ""
