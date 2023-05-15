#!/usr/bin/python3
"""User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """call the super class with the args"""
        super().__init__(**kwargs)
