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

    prompt = '(HBNB) '

    def do_quit(self, arg):
        """exit from HBNB console
        """
        return True

    def do_EOF(self, arg):
        """EOF command for forcing exit
        """

        return True

    def emptlyline(self):
        """Handles the emplty line
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
