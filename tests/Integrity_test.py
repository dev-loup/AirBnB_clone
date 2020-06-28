#!/usr/bin/python3
"""
    Integrity Test module: check if all files are present
    TestClasses:
        FileTest: test AirBnb files are completed
"""

import unittest
import os


class FileTest(unittest.TestCase):
    """ Test if all modules & packages are reachable
    """
    files = ['README.md', 'AUTHORS', 'tests/',
             'models/base_model.py', 'models/__init__.py',
             'models/engine/file_storage.py',
             'models/engine/__init__.py', 'console.py',
             'models/user.py', 'models/state.py',
             'models/city.py', 'models/amenity.py',
             'models/place.py', 'models/review.py']

    def test_file_present(self):
        """ Test existance of all needed elements
        """

        for path in self.files:
            with self.subTest(path=path):
                self.assertEqual((os.path.isfile(path)
                                  or os.path.isdir(path)), True)
