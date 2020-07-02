#!/usr/bin/python3
""" City Class module.
    Set an HBNB City parameters
    Classes:
        User: stores all the data of a new city
"""

from models.base_model import BaseModel


class City(BaseModel):
    """ Defines attributes and parameters of user class
        Public Class Attributes:
            name: city's name
    """

    state_id = ""
    name = ""
