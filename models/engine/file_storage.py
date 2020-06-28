#!/usr/bin/python3
""" Storage Module.
    Manage Json files serializations & storage
    Classes:
        FileStorage: serialization of JSON files
"""

import os
import json
import sys
from models.base_model import BaseModel


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
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serialize __objects to JSON FILE
        """

        cast__objects = dict()
        for key in FileStorage.__objects.keys():
            cast__objects[key] = FileStorage.__objects[key].to_dict()
        json_string = json.dumps(cast__objects)
        with open(FileStorage.__file_path, 'w+') as docfile:
            docfile.write(json_string)

    def reload(self):
        """ load a JSON FILE to __objects
        """
        if os.path.isfile(FileStorage.__file_path) is False:
            return
        with open(FileStorage.__file_path, 'r') as docfile:
            doc_read = docfile.read()
            if len(doc_read) == 0:
                return
            dict_load = json.loads(doc_read)
            for inst in dict_load.keys():
                inst_class = inst.split('.')
                FileStorage.new(self, getattr(sys.modules[__name__],
                                inst_class[0])(**dict_load[inst]))
