#!/usr/bin/python3
"""This module contains a script that adds all arguments
to a Python list, and then save them to a file
"""
import sys
save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]

existing_json = load_from_json("add_item.json") or []

new_items = existing_json + args

save_to_json(new_items, "add_item.json")
