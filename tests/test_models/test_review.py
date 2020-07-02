#!/usr/bin/python3
"""
    Review Test module: Check State instance
    TestClasses:
        AttributesTest: test attributes assign & working
"""

import unittest
from models.base_model import BaseModel
from models.review import Review
import uuid
import datetime


class AttributesTest(unittest.TestCase):
    """ Test if attributes in class are working fine
    """

    def test_review(self):
        """ test name attr existance
        """

        dummy = Review()
        self.assertIsNotNone(dummy.place_id)
        self.assertIsNotNone(dummy.user_id)
        self.assertIsNotNone(dummy.text)
