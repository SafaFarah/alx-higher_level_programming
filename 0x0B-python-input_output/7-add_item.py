#!/usr/bin/python3
"""
Defines a script that adds all arguments to a
Python list, and then save them to a file.
"""


import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
args_list = sys.argv
filename = "add_item.json"
try:
    _list = load_from_json_file(filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
    _list = []
_list.extend(args_list[1:])
save_to_json_file(_list, filename)
