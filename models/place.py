#!/usr/bin/python3
""" Place Class module.
    Set an HBNB Full Place parameters
    Classes:
        Place: stores all the place attributes
"""

from models import base_model


class Place(base_model.BaseModel):
    """ Defines attributes and parameters of user class
        Public Class Attributes:
            city_id: cities identification
            user_id: user identification
            name: place's name
            description: place's description
            number_rooms: number of rooms
            number_bathrooms: number of baths
            max_guest: limit of guests
            price_by_night: night price
            latitude: lat ° of place
            longitude: long° of place
            amenity_ids: amenities id
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
