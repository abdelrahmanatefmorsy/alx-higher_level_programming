#!/usr/bin/python3
"""modules"""
import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


mylist = list(sys.argv[1:])
try:
    s = load('add_item.json')
except Exception:
    s = []

s.extend(mylist)
save(s, 'add_item.json')
