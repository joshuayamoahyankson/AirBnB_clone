#!/usr/bin/python3
"""A command interpreter class"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for HBNB"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """This quits or exits the program in action"""
        return True

    def do_EOF(self, arg):
        """This is the end of file(EOF) function to exit the running program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def help_cmd(self, arg):
        """A help command to guide the user if there
        be any need for assistance on a particular function
        """
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id."""
        if not arg:
            print("** class name missing **")
            return

        if arg not in storage.classes():
            print("** class doesn't exist **")
            return

        # Create and save the new instance
        instance = storage.classes()[arg]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        line = arg.split()
        if len(line) == 0:
            print("** class name missing **")
            return
        class_name = line[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(line) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        instance = storage.all()[key]
        print(instance)

    def do_destroy(self, line):
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        args = line.split()
        if len(args) > 0:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return
            instances = [
                str(obj) for key, obj in storage.all().items()
                if key.startswith(class_name)
            ]
        else:
            instances = [
                    str(obj) for obj in storage.all()
                    .values()
            ]
            print(instances)

    def do_update(self, line):
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3].strip('"')
        instance = storage.all()[key]
        # Convert the attribute value to the appropriate type
        if attr_value.isdigit():
            attr_value = int(attr_value)
        else:
            try:
                attr_value = float(attr_value)
            except ValueError:
                pass
        setattr(instance, attr_name, attr_value)
        instance.save()
