#!/usr/bin/python3
"""City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class"""
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """call the super class with the args"""
        super().__init__(**kwargs)
