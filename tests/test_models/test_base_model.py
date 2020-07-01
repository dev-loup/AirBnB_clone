#!/usr/bin/python3
"""
    Integrity Test module: check if all files are present
    TestClasses:
        AttributesTest: test attributes assign & working
"""

import unittest
from models.base_model import BaseModel
import uuid
import datetime


class AttributesTest(unittest.TestCase):
    """ Test if attributes in class are working fine
    """

    def test_id(self):
        """ Test proper id working
            Attributes tested:
                Basemodel.id
        """

        dummy = BaseModel()
        self.assertIsInstance(uuid.UUID(dummy.id), uuid.UUID)
        self.assertIsInstance(dummy.id, str)

    def test_datetime(self):
        """ Test Attributes of date
            Attributes Tested:
                BaseModel.created_at
                BaseModel.updated_at
        """

        dummy = BaseModel()
        self.assertIsInstance(dummy.created_at, datetime.datetime)
        self.assertIsInstance(dummy.updated_at, datetime.datetime)


class MethodsTest(unittest.TestCase):
    """ Test correct working of methods
        Methods:
            __str__
            save
            to_dict
    """

    def test_str(self):
        """ Test __str__ behaviour & working
        """

        dummy = BaseModel()
        str_dummy = "{}".format(dummy)
        str_expected = "[{}] ({}) {}".format(dummy.__class__.__name__,
                                             dummy.id,
                                             str(dummy.__dict__))
        self.assertIsInstance(str_dummy, str)
        self.assertEqual(str_dummy, str_expected)

    def test_save(self):
        """ test proper save working
        """

        dummy = BaseModel()
        init_date = dummy.updated_at
        dummy.save()
        final_date = dummy.updated_at
        self.assertNotEqual(init_date, final_date)

    def test_to_dict(self):
        """ Test to_dict method
        """

        dummy = BaseModel()
        dict_dummy = dummy.to_dict()
        self.assertIsInstance(dict_dummy, dict)
        self.assertEqual(dict_dummy["__class__"], dummy.__class__.__name__)
        self.assertNotIsInstance(dict_dummy["created_at"], datetime.datetime)
        self.assertNotIsInstance(dict_dummy["updated_at"], datetime.datetime)

    def test_init(self):
        """ Test recreation of instances from dicts
        """

        dummy = BaseModel()
        dict_dummy = dummy.to_dict()
        new_dummy = BaseModel(**dict_dummy)
        self.assertEqual("{}".format(dummy), "{}".format(new_dummy))
