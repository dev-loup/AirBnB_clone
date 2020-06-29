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

    def __init__(self):
        """ class constructor
        """

        cmd.Cmd.__init__(self)
        self.intro = r"""
        HbNB Clone command interpreter
        -----------------------------
                Welcome Human """
        self.prompt = '(HBNB) '

    def do_quit(self, arg):
        """exit from HBNB console
        """

        sys.exit()

    def do_EOF(self, arg):
        """EOF command for forcing exit
        """

        return True


HBNBConsole = HBNBCommand()
HBNBConsole.cmdloop()
