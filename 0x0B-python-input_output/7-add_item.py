#!/usr/bin/python3
"""A script that adds command-line arguments to a list and
saves it to a JSON file.

This script loads a list from add_item.json (or creates an
empty list if not found),
appends all arguments (sys.argv[1:]) to it, and saves the
updated list back to the file.
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []
items.extend(sys.argv[1:])
save_to_json_file(items, filename)
