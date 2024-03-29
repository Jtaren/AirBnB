#!/bin/python3

import cmd

class UserMaagement(cmd.Cmd):
    """simple CRUD command for managing users""" 

    prompt = "shell $ " 
    def __init__(self):
        super().__init__()
        self.users = {} #dictionary to store users

    def do_create(self, line):
        """create a new user Syntax: create <digit> <name>"""
        args = line.split()
        if len(args) == 2:
            digit, name = args
            self.users[digit] = name
            print(f"User created - ID: {digit}, Name: {name}")
        else:
            print("The input is not valid")
    def do_read(self, line):
        """Read and Display all users"""
        print("list of users:")
        for digit, name in self.users.items():
            print(f"ID: {digit}, Name: {name}")

    def do_update(self, line):
        """Update user's name, Syntax: create <digit> <name>"""
        args = line.split()
        if len(args) == 2:
            digit, name = args
            if digit in self.users:
                self.users[digit] = name
                print(f"User update - ID: {digit}, Nmae: {name}")
            else:
                print(f"No user found with - ID {digit}")
        else:
            print("Invalid input, use: update <digit> <name>")

    def do_delete(self, line):
        """Delete a User by ID. Syntax: Update <digit> <name>"""
        if line in self.users:
            del self.users[line]
            print(f"User deleted - ID {line}")
        else:
            print(f"No user found with ID {line}")

    
if __name__ == '__main__':
    UserMaagement().cmdloop()