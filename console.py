#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """ """


    def do_EOF(self, line):
        """exit cli"""
        return TRUE

    def do_quit(self, line):
        """quits the cli"""
        return TRUE
if __name__ == '__main__':
    HBNBCommand().cmdloop()
