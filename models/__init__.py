#!/usr/bin/python3
""" Models module init
    Modules:
        file_storage.py
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
