#!/usr/bin/python3
"""Function begins from here."""


def is_same_class(obj, a_class):
    """Inside of function."""
    return isinstance(obj ,a_class) and type(obj) is not a_class
