#!/usr/bin/python3

from models.base_model import BaseModel

class City(BaseModel):
    """City class"""
    name = ""
    state_id = ""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)