#!/usr/bin/python3
"""
    FileStorage Test module: check if all files are present
    TestClasses:
        AttributesTest: test attributes assign & working
"""

import unittest
from models.base_model import BaseModel
from models import storage
import os
import json


class AttributesTest(unittest.TestCase):
    """ Test if attributes in class are working fine
    """

    pass


class MethodsTest(unittest.TestCase):
    """ Test proper FileStorage method working
    """

    def test_all(self):
        """ Test all method
        """

        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        """ Test new method
        """

        dummy = BaseModel()
        storage.new(dummy)
        key = "{}.{}".format(dummy.__class__.__name__, dummy.id)
        self.assertTrue(storage.all()[key])

    def test_saving(self):
        """ Test saving a
        """

        self.assertIsInstance(storage.all(), dict)
        obj_size_one = len(storage.all())
        dummy = BaseModel()
        dummy.save()
        obj_size_two = len(storage.all())
        self.assertNotEqual(obj_size_one, obj_size_two)

    def test_reload(self):
        """ Test Reloading method
        """

        obj_size_one = len(storage.all())
        if os.path.isfile('file.json'):
            with open('file.json', 'r') as docfile:
                docread = docfile.read()
                if len(docread) > 0:
                    storage.reload()
                    obj_size_two = len(storage.all())
                    self.assertNotEqual(obj_size_one, obj_size_two)
                else:
                    storage.reload()
                    obj_size_two = len(storage.all())
                    self.assertEqual(obj_size_one, obj_size_two)
