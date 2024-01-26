#!/usr/bin/python3

"""
This script takes GitHub credentials (username and personal access token) as
command-line arguments, uses Basic Authentication with the GitHub API to
display the user's ID.
"""

import requests
import sys

if len(sys.argv) != 3:
    sys.exit("Usage: ./10-my_github.py <username> <personal_access_token>")

username = sys.argv[1]
token = sys.argv[2]

url = 'https://api.github.com/user'
response = requests.get(url, auth=(username, token))

try:
    user_data = response.json()
    user_id = user_data.get('id')
    print(user_id)

except ValueError:
    print(None)
