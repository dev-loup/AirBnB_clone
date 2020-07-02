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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
