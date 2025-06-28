#!/usr/bin/python3
"""Function is starting!"""
import json


def save_to_json_file(my_obj, filename):
    """It is inside of function."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
