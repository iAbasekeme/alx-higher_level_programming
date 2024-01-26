#!/usr/bin/python3
"""A script that fetches a url
"""

if __name__ == "__main__":
    import urllib.request
    with urllib.request.\
            urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read().decode('utf-8')

        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
