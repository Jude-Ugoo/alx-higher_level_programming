#!/usr/bin/pythoni3

def new_in_list(my_list, idx, element):
    dup_list = my_list.copy()

    if idx < 0 or idx >= len(my_list):
        return my_list

    while idx < len(my_list):
            dup_list[idx] = element
            return dup_list
