#!/usr/bin/python3
""" User Class module.
    Set an HBNB User parameters
    Classes:
        User: stores all the data of a new user
"""

from models.base_model import BaseModel


class User(BaseModel):
    """ Defines attributes and parameters of user class
        Public Class Attributes:
            email: stores email data
            password: stores password
            first_name: stores first_name
            last_name: stores last_name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
