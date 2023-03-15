#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_set = set(my_list)
    total = 0
    for item in new_set:
        total += item
    return total
