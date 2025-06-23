#!/usr/bin/python3
class Square:
    def __init__(self, size):
        self.__size = size

    def getSize(self):
        print("Getter received")
        return self.__size

    def setSize(self, value):
        print("Setter received")
        self.__size = value
