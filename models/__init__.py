#!/usr/bin/python3
""" import file_storage variable """
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
storage.reload()
