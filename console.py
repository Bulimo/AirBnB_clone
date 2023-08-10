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

    def do_create(self, arg):
        """Creates a new instance of BaseModel

        Args:
            arg (_type_): _description_
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of
        an instance based on the class name

        Args:
            arg (_type_): _description_
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        instances = storage.all()

        if key in instances:
            print(instances[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id

        Args:
            arg (_type_): _description_
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        instances = storage.all()

        if key in instances:
            del instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name

        Args:
            arg (_type_): _description_
        """
        args = arg.split()
        instances = storage.all()

        if not args:
            print([str(instance) for instance in instances.values()])
        elif args[0] in storage.classes:
            print([str(instance) for key, instance in instances.items()
                  if key.startswith(args[0] + ".")])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class
        name and id by adding or updating attribute

        Args:
            arg (_type_): _description_
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        instances = storage.all()

        if key not in instances:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        instance = instances[key]
        setattr(instance, args[2], args[3])
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
