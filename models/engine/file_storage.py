#!/usr/bin/python3
""" Storage Module.
    Manage Json files serializations & storage
    Classes:
        FileStorage: serialization of JSON files
"""

import os
import json


class FileStorage():
    """ Manage JSON serialization & storage in files
        Private Class Attributes:
            __file_path: JSON location
            __objects: dictionary for objects storage
        Public Instance methods:
            all(self): return dict __objects
            new(self, obj): store an object in __objects
            save(self): serializes __objects to JSON FILE
            reload(self): deserializes JSON FILE to __objects
    """

    __file_path = 'file.json'
    __objects = dict()

    def all(self):
        """ Returns the dictionary __objects
        """

        return FileStorage.__objects

    def new(self, obj):
        """ Set an object into __objects
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        packed_object = (key, obj)
        FileStorage.__objects.update(packed_object)

    def save(self):
        """ Serialize __objects to JSON FILE
        """

        casted_dict = dict()
        for key in __objects.keys():
            casted_dict[key] = _objects[key].to_dict()
        json_string = json.dumps(casted_dict)
        with open(FileStorage.__file_path, 'w') as docfile:
            docfile.write(json_string)

    def reload(self):
        """ load a JSON FILE to __objects
        """
        if os.path.isfile(FileStorage.__objects) is False:
            return FileStorage.__objects
        with open(FileStorage.__file_path, 'r') as docfile:
            FileStorage.__objects = dict()
