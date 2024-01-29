#!/usr/bin/python3
"""Docs
"""
from sys import argv

if __name__ == "__main__":

    api_url = f'https://api.github.com/user/{argv[1]}'

    # Set up Basic Authentication using the personal access token
    auth = HTTPBasicAuth(argv[1], argv[2])

    try:
        # Make the API request
        response = requests.get(api_url, auth=auth)

        # Check if the request was successful (status code 200 OK)
        if response.status_code == 200:
            user_info = response.json()
            user_id = user_info.get('id', 'N/A')
            print(f"{user_id}")
        else:
            print("None")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
