#!/usr/bin/python3
""" HbNB command interpreter
    Classes:
        HBNBCommand: HbBN Console
"""

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """ Command interpreter for HbNB clone
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF command for forcing exit
        """

        return True

    def emptyline(self):
        """Handles the emplty line
        """

        pass

    def do_create(self, args):
        """creates a new instance of a given class
        """
        if len(args) == 0:
            print('** class name missing **')
            return
        arg_l = args.split()
        try:
            new = eval(arg_l[0])()
            print(new.id)
            new.save()
        except Exception:
            print("** class doesn't exist **")
            return

    def do_show(self, args):
        """Prints str rep of an instance
        """
        models.storage.reload()
        if len(args) == 0:
            print('** class name missing **')
            return
        args_l = args.split()
        try:
            elem = eval(args_l[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(args_l) == 1:
            print("** instance id missing **")
            return
        elif len(args_l) > 1:
            k = args_l[0] + "." + args_l[1]
            if k in models.storage.all():
                print(models.storage.all()[k])
            else:
                print("** no instance found **")
                return

    def do_destroy(self, args):
        if len(args) == 0:
            print('** class name missing **')
            return
        args_l = args.split()
        try:
            elem = eval(args_l[0])
        except Exception:
            print("** instance id missing **")
            return
        if len(args_l) == 1:
            print('** instance id missing **')
            return
        elif len(args_l) > 1:
            k = args_l[0] + '.' + args_l[1]
            if k in models.storage.all():
                models.storage.all().pop(k)
                models.storage.save()
            else:
                print('** no instance found **')
                return

    def do_all(self, args):
        """ Display all instances based on given class name
        """
        models.storage.reload()
        if len(args) < 1:
            ac = []
            for value in models.storage.all().values():
                ac.append(str(value))
            if not ac:
                return
            print(ac)
        else:
            modelClass = args.split(" ")
            if modelClass[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif modelClass[0] in HBNBCommand.classes:
                ac = []
                for value in models.storage.all().values():
                    if modelClass[0] in value.__class__.__name__:
                        ac.append(str(value))
                if not ac:
                    return
                print(ac)

    def do_update(self, args):
        """ update an instance by its UUID
        """
        args_l = args.split()
        if len(args_l) == 0:
            print("** class name missing **")
        elif (args_l[0] not in self.classes):
            print("** class doesn't exist **")
        elif len(args_l) == 1:
            print("** instance id missing **")
            return
        else:
            try:
                key = args_l[0] + '.' + args_l[1]
                storage.all()[key]
            except KeyError:
                print('** no instance found **')
                return
            if len(args_l) == 2:
                print("** attribute name missing **")
                return
            elif len(args_l) == 3:
                print("** value missing **")
                return
            else:
                key = args_l[0] + '.' + args_l[1]
                try:
                    if '.' in args_l[3]:
                        value = float(args_l[3])
                    else:
                        value = int(args_l[3])
                except ValueError:
                    value = str(args_l[3]).strip("\"':")
                    value = str(value)
                    setattr(storage.all()[key], args_l[2].strip("\"':"), value)
                    storage.save()
if __name__ == '__main__':
    HBNBCommand().cmdloop()
