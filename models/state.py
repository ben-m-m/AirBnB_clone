#!/usr/bin/python3
"""State class"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class"""
    name = ""

    def __init__(self, **kwargs):
        """call the super class with the args"""
        super().__init__(**kwargs)
