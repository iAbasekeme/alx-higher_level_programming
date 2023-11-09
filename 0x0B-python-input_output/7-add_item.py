# 7-add_item.py
import sys

save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]
print(args)

existing_json = []
existing_json = load_from_json("add_item.json")

new_items = existing_json + args

save_to_json(new_items, "add_item.json")
