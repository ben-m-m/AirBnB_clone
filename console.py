#!/usr/bin/python3
import cmd
import json


class HBNBCommand(cmd.Cmd):
    """ """

    prompt = '(hbnb)'
    classes = ['Basemodel',]

    def do_create(self, class_name):
        """Creates new instance of BaseModel, saves it(JSON file), prints id"""
        if class_name == '':
            print("** class name missing **")
        if class_name != classes:
            print("** class doesn't exist **")

    def do_show(self, class_name, class_id):
        """Prints the string repr. of an instance based on class name and id"""
        if class_name == '':
            print("** class name missing **")
        elif class_name != classes:
            print("** class doesn't exist **")
        elif class_id == '':
            print("** instance id missing **")
        elif class_id != classes[i].id:
            print("** no instance found **")
        else:
            print("{}.{}".format(class_name, class_id))

    def do_destroy(self, class_name, class_id):
        """Deletes an instance based on the class name and id(save to JSON)"""
        if class_name == '':
            print("** class name missing **")
        elif class_name != classes:
            print("** class doesn't exist **")
        elif class_id == '':
            print("** instance id missing **")
        elif class_id != classes[i].class_id:
            print("** no instance found **")

    def do_all(self, class_name):
        if class_name != classes:
            print("** class doesn't exist **")
        else """returning string rep"""

    def do_all():

        pass

    def do_update(self, ):

    def do_EOF(self, line):
        """exit cli"""
        return True

    def do_quit(self, line):
        """quits the cli"""
        return True

    def emptyline(self):
        """do nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
