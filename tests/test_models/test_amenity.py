#!/usr/bin/python3
"""
    Amenity Test module: Check amenity instance
    TestClasses:
        AttributesTest: test attributes assign & working
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
import uuid
import datetime


class AttributesTest(unittest.TestCase):
    """ Test if attributes in class are working fine
    """

    def test_amenity(self):
        """ test name attr existance
        """

        dummy = Amenity()
        self.assertIsNotNone(dummy.name)
