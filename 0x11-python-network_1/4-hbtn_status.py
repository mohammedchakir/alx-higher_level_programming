#!/usr/bin/python3

"""
This script fetches https://alx-intranet.hbtn.io/status using the requests package
and displays information about the response body.
"""

import requests

url = 'https://alx-intranet.hbtn.io/status'

response = requests.get(url)

print("Body response:")
print("\t- type:", type(response.text))
print("\t- content:", response.text)
