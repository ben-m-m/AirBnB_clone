#!/usr/bin/python3

from models.base_model import BaseModel

class User(BaseModel):
    """User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)