#!/usr/bin/python3
"""Docs
"""
import requests
from sys import argv

if __name__ == "__main__":
    q = argv[1] if len(argv) > 1 else ""
    data = {'q': q}

    res = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        json_data = res.json()
        if json_data:
            user_id = json_data.get('id', 'N/A')
            user_name = json_data.get('name', 'N/A')
            print("[{}] {}".format(user_id, user_name))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
