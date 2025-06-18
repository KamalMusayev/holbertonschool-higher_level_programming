#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    if idx < 0 or idx >= len(my_list):
        return my_list
    for num in my_list:
        if num != idx:
            new_list.append(num)
    return new_list
