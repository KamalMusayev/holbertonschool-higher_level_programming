#!/usr/bin/python3
"""Function is starting!"""
import json


def load_from_json_file(filename):
    """It is inside of function."""
    with open(filename, "r", encoding="utf-8") as f:
        json.load(f)
