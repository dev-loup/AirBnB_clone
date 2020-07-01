#!/usr/bin/python3
""" State Class module.
    Set an HBNB State parameter
    Classes:
        State: stores all the data of a new state
"""

from models import base_model


class State(base_model.BaseModel):
    """ Defines attributes and parameters of State class
        Public Class Attributes:
            name: State's name
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
