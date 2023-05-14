#!/usr/bin/python3
"""Amenity class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""
    name = ""

    def __init__(self, **kwargs):
        """call the super class with the args"""
        super().__init__(**kwargs)
