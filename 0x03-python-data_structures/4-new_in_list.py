#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    dup_list = my_list.copy()

    if idx < 0 or idx >= len(my_list):
        return my_list

    for i in dup_list:
        if i == idx:
            dup_list[idx] = element
            return dup_list
