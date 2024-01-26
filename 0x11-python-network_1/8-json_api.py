#!/usr/bin/python3

"""
This script takes a letter as a command-line argument, sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter using the
requests package, and processes the JSON response accordingly.
"""

import requests
import sys

if len(sys.argv) < 2:
    q = ""
else:
    q = sys.argv[1]

url = 'http://0.0.0.0:5000/search_user'
data = {'q': q}

response = requests.post(url, data=data)

try:
    json_data = response.json()
    if json_data:
        print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
    else:
        print("No result")

except ValueError:
    print("Not a valid JSON")
