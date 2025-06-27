#!/usr/bin/python3
def read_file(filename=""):
    """FUnction begins from here."""
    with open(f"{filename}", encoding='UTF8') as f:
        print(f.read, end="")
