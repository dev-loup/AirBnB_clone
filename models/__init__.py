#!/usr/bin/python3
""" Engine module init
    Modules:
        file_storage.py
"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
