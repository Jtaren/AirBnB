#!/bin/bash/python3
import cmd

class Command(cmd.Cmd):
    
    """This is a simple command line interpreter"""

    prompt = "console>>>"
    def do_greet(self, line):
        """Greet the name <person>"""
        if line:
            print("Hello,", line)
        else:
            print("Hi")
    def help_greet(self):
        print('\n'.join([
            'greet [person]',
        ]))

    def do_EOF(self, line):
        """Exit the console gracefully"""
        print()
        return True
    
    def default(self, line):
        print(f"Unknown command: {line}")

    def emptyline(self):
        print("You have entered empty line")

    def do_quit(self, line):
        return True
    
    def help_quit(self, line):
        print("Quit the console")
if __name__ == '__main__':
    Command().cmdloop()
