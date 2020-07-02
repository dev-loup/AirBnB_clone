#!/usr/bin/python3
""" Place Class module.
    Set an HBNB Full Place parameters
    Classes:
        Place: stores all the place attributes
"""

from models.base_model import BaseModel


class Place(BaseModel):
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

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
