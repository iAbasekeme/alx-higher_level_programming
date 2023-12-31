#!/usr/bin/python3
"""This module contains a script that adds all arguments
to a Python list, and then save them to a file
"""
import sys
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if exists("add_item.json"):
    updated_data = load_from_json_file("add_item.json")
else:
    updated_data = []
    for arg in sys.argv[1:]:
        updated_data.append(arg)

save_to_json_file(updated_data, "add_item.json")
