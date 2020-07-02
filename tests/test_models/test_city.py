#!/usr/bin/python3
"""
    City Test module: Check city instance
    TestClasses:
        AttributesTest: test attributes assign & working
"""

import unittest
from models.base_model import BaseModel
from models.city import City
import uuid
import datetime


class AttributesTest(unittest.TestCase):
    """ Test if attributes in class are working fine
    """

    def test_city(self):
        """ test name attr existance
        """

        dummy = City()
        self.assertIsNotNone(dummy.state_id)
        self.assertIsNotNone(dummy.name)
