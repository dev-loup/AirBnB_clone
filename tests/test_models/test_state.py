#!/usr/bin/python3
"""
    State Test module: Check State instance
    TestClasses:
        AttributesTest: test attributes assign & working
"""

import unittest
from models.base_model import BaseModel
from models.state import State
import uuid
import datetime


class AttributesTest(unittest.TestCase):
    """ Test if attributes in class are working fine
    """

    def test_state(self):
        """ test name attr existance
        """

        dummy = State()
        self.assertIsNotNone(dummy.name)
