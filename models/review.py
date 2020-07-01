#!/usr/bin/python3
""" Place Class module.
    Set an HBNB Full Place parameters
    Classes:
        Review: stores all the place attributes
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ Defines attributes and parameters of Review class
        Public Class Attributes:
            place_id: place's identification
            user_id: user who reviewed
            text: the review
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
