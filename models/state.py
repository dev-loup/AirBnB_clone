#!/usr/bin/python3
""" State Class module.
    Set an HBNB State parameter
    Classes:
        State: stores all the data of a new state
"""

from models.base_model import BaseModel


class State(BaseModel):
    """ Defines attributes and parameters of State class
        Public Class Attributes:
            name: State's name
    """

    name = ""
