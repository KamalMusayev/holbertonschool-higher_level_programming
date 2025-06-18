#!/usr/bin/python3
def multiple_returns(sentence):
    first = sentence[0]
    length = len(sentence)
    if len(sentence) == 0:
        first = None
    return length , first
