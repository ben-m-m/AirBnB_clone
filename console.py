#!/usr/bin/python3
""" import file_storage variable """


import cmd
from datetime import datetime
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb) '
    __classes = ["BaseModel"]
    __dict = {}
    __classes_id = []
    
    def state(self, args):
        """state method"""
        args = args.split()
        self.__dict = storage.all()
        self.__classes_id = list(self.__dict.keys())
        return args
    
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
        if arg == "":
            print("** class name missing **")
        elif arg not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(arg)()
            print(new_obj.id)
            storage.save()
    
    def do_show(self, arg):
        args = self.state(arg)
        # print(self.__dict)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in self.__classes_id:
            print("** no instance found **")
        else:
            # print(type(args[0] + "." + args[1]))
            print(self.__dict[args[0] + "." + args[1]])
    
    def do_destroy(self, arg):
        args = self.state(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in self.__classes_id:
            print("** no instance found **")
        else:
            # print(type(args[0] + "." + args[1]))
            storage.delete(self.__dict[args[0] + "." + args[1]])
            self.__dict = storage.all()
            self.__classes_id = list(self.__dict.keys())
        
    def do_all(self, arg):
        args = self.state(arg)
        list = []
        if len(args) == 1 or len(args) == 0:
            for value in self.__dict.values():
                list.append(str(value))
            print(list)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
