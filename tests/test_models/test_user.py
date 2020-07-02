#!/usr/bin/python3
"""
    User Test module: Check Place instance
    TestClasses:
        AttributesTest: test attributes assign & working
"""

import unittest
from models.base_model import BaseModel
from models.user import User
import uuid
import datetime


class AttributesTest(unittest.TestCase):
    """ Test if attributes in class are working fine
    """

    def test_place(self):
        """ test name attr existance
        """

        dummy = User()
        self.assertIsNotNone(dummy.email)
        self.assertIsNotNone(dummy.password)
        self.assertIsNotNone(dummy.first_name)
        self.assertIsNotNone(dummy.last_name)
