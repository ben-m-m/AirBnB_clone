#!/usr/bin/python3
""" import file_storage variable """


import cmd
from datetime import datetime
from typing import Any
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = '(hbnb) '
    intro = 'this is a command line interpreter for AirBnB project'

    __classes = {"BaseModel": BaseModel,
                 "User": User,
                 "State": State,
                 "City": City,
                 "Amenity": Amenity,
                 "Place": Place,
                 "Review": Review}
    __cli_kwargs = {}

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        return True

    def emptyline(self):
        """emptyline method"""
        pass

    def do_create(self, arg):
        """creates a new instance of entered class name as argument and prints the id"""
        if arg == "":
            print("** class name missing **")
        elif arg not in self.__classes.keys():
            print("** class doesn't exist **")
        else:
            for k, v in self.__classes.items():
                if arg == k:
                    print(v(self.__cli_kwargs).id)

    def do_show(self, arg):
        """Prints the string of an instance based on the class name and id you input"""
        args, store_key = self.__split_key(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif store_key not in storage.all().keys():
            print("** no instance found **")
        else:
            for k, v in storage.all().items():
                if store_key == k:
                    print(v)

    def do_destroy(self, arg):
        """deletes an instance based on the class name and id input"""
        args, store_key = self.__split_key(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif store_key not in storage.all().keys():
            print("** no instance found **")
        else:
            try:
                for k, v in storage.all().items():
                    if store_key == k:
                        storage.delete(k)
            except RuntimeError:
                pass

    def do_all(self, arg):
        """prints all instances or instances of the class name that you input"""
        args = arg.split()
        if len(args) == 0:
            [print(val) for key, val in storage.all().items()]
        elif len(args) == 1:
            if args[0] not in self.__classes.keys():
                print("** class doesn't exist **")
            elif args[0] in self.__classes.keys():
                [print(val) for key, val in storage.all().items() if arg[0] in key]

    def do_update(self, arg):
        """updates an instance based on the class name and id by adding or updating 
        an attribute and its value"""
        args, store_key = self.__split_key(arg)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif store_key not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** no attribute found **")
        elif len(args) == 3:
            print("** no attribute value found **")
        else:
            attr = args[2]
            attr_val = args[3]
            try:
                for k, v in storage.all().items():
                    if store_key == k:
                        storage.update(k, attr, attr_val)
            except RuntimeError:
                pass

    def __split_key(self, arg):
        args = arg.split()
        if len(args) == 1:
            return args, None
        return args, args[0] + "." + args[1]

    def completedefault(self, text, *ignored: Any) -> list[str]:
        b = [storage.getid(k) for k, v in storage.all().items()]
        return [a for a in self.__classes.keys() if a.startswith(text)] +\
            [a for a in b if a.startswith(text)]

    def default(self, line):
        arg = line.split(".")
        self.do_all(arg[0])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
