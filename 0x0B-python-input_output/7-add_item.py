#!/usr/bin/python3

"""Imports multiple python modules."""


import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

args = sys.argv[1:]
data = load_from_json_file("add_item.json")
data += args

save_to_json_file(data, "add_item.json")

print(load_from_json_file("add_item.json"))
