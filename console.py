#!/usr/bin/python3
""" HbNB command interpreter
    Classes:
        HBNBCommand: HbBN Console
"""

import cmd
import sys


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
