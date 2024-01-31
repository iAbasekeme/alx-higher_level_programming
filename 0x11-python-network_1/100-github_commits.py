#!/usr/bin/python3
"""
takes 2 arguments in order to solve this challenge.
"""
import requests
from sys import argv


if __name__ == '__main__':
    repo = argv[1]
    name = argv[2]
    url = f'https://api.github.com/repos/{name}/{repo}/commits'

    req = requests.get(url)

    result = req.json()
    for commit in result[:10]:
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author_name}")
