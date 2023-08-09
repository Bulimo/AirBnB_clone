#!/usr/bin/python3
"""
Commandline interpreter module
Defines class HBNBCommand()
"""
import cmd
import readline


class HBNBCommand(cmd.Cmd):
    """
    Class to carry out commands for the AirBnb project

    Args:
        cmd: Commands module
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """
        Do nothing if no command is passed
        """

        pass

    def do_EOF(self, arg):
        """
        End the program when Ctrl+D is pressed

        Returns:
            True
        """

        print()
        return True

    def do_quit(self, arg):
        """
        End the program when Ctrl+D is pressed

        Returns:
            True
        """

        return True

    def help_quit(self):
        """
        Documentation for the quit command
        """

        print("Usage: quit")
        print("command exits the comand line interpreter program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
