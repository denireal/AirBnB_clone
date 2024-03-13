"""Importing the FileStorage class from the file_storage module within
the models.engine package
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
