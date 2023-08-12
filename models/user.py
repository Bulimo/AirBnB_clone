#!/usr/bin/python3
"""
Module that defines class User
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines the class representing a user
    Inherits from the BaseModel class
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """_summary_
        """
        super().__init__(*args, **kwargs)
