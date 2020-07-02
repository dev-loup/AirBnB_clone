#!/usr/bin/python3
""" HbNB command interpreter
    Classes:
        HBNBCommand: HbBN Console
"""

from cmd import Cmd
import sys


class HBNBCommand(Cmd):
    """ Command interpreter for HbNB clone
    """

    prompt = '(HBNB) '

    def do_quit(self, arg):
        """exit from HBNB console
        """
        return True

    def do_EOF(self, arg):
        """EOF command for forcing exit
        """

        return True

    def do_emptlyline(self):
        return None


if __name__ == '__main__':
    HBNBCommand().cmdloop()
