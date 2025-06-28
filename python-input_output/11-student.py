#!/usr/bin/python3
"""Class start from here!."""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Inside of Class
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            filtered = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filtered[attr] = getattr(self, attr)
            return filtered
        else:
            return self.__dict__.copy()

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
