#!/usr/bin/python3
""" Amenity Class module.
    Set an HBNB State parameter
    Classes:
        Amenity: create an Amenity class with name
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Defines attributes and parameters of State class
        Public Class Attributes:
            name: Amenity's name
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
