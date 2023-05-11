#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """ """

    prompt = '(hbnb)'

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
