#!/usr/bin/python3
""" SuperClass module.
    Define common attributes and methods for AirBnB console
    Classes:
        BaseModel: set common attributes & methods
"""

from uuid import uuid4
import datetime
import models


class BaseModel():
    """ Define common attributes and methods for AirBnB console.
        Public instance attributes:
            id: unique id number, assigned with uuid.
            created_at: datetime assigned with the current date.
            updated_at: datetime assigned on creation or edition.
            __str__: custom str method prints readable class.
        Public instance methods:
            save(self): updates the public instance attribute update_at.
            to_dict(self): returns a dictionary with all key/values in
                            __dict.
    """

    def __init__(self, *args, **kwargs):
        """ instance constructor
        """

        if len(kwargs) > 0:
            for key in kwargs.keys():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key,
                            datetime.datetime.fromisoformat(kwargs[key]))
                else:
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Print a readable representation of class
            Format:
                [<class name>] (<self.id>) <self.__dict__>
        """

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at
        """

        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Return a dictionary type data from class
        """

        proto_dict = dict(self.__dict__)
        proto_dict["__class__"] = self.__class__.__name__
        proto_dict["created_at"] = self.created_at.isoformat()
        proto_dict["updated_at"] = self.updated_at.isoformat()

        return proto_dict
