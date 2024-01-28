#!/usr/bin/python3
"""Docs
"""
from urllib import requests
from sys import argv

if __name__ == "__main__":
    data = argv[1]
    q = data if len(sys.argv) > 1 else ""
    requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    json_data = response.json()
    if json_data:
        user_id = json_data.get('id', 'N/A')
        user_name = json_data.get('name', 'N/A')
        print("[{}] {}".format(user_id, user_name))
    else:
        print("No result")
