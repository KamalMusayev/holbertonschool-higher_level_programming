#!/usr/bin/python3
"""Function begins from here."""


def is_same_class(obj, a_class):
    """Inside of function."""
    return type(obj) is  a_class or type(obj) is a_class(obj)
