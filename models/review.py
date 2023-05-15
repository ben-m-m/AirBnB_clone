#!/usr/bin/python3
"""Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """call the super class with the args"""
        super().__init__(**kwargs)
