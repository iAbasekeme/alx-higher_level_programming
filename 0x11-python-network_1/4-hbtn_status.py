#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
"""
import request

if __name__ == "__main__":
    r = request.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r)))
    print(f"\t- content: {r}")
