#!/usr/bin/python3
"""
    Place Test module: Check Place instance
    TestClasses:
        AttributesTest: test attributes assign & working
"""

import unittest
from models.base_model import BaseModel
from models.place import Place
import uuid
import datetime


class AttributesTest(unittest.TestCase):
    """ Test if attributes in class are working fine
    """

    def test_place(self):
        """ test name attr existance
        """

        dummy = Place()
        self.assertIsNotNone(dummy.city_id)
        self.assertIsNotNone(dummy.user_id)
        self.assertIsNotNone(dummy.name)
        self.assertIsNotNone(dummy.description)
        self.assertIsNotNone(dummy.number_rooms)
        self.assertIsNotNone(dummy.number_bathrooms)
        self.assertIsNotNone(dummy.max_guest)
        self.assertIsNotNone(dummy.price_by_night)
        self.assertIsNotNone(dummy.latitude)
        self.assertIsNotNone(dummy.longitude)
        self.assertIsNotNone(dummy.amenity_ids)
