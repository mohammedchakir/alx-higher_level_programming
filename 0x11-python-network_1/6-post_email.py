#!/usr/bin/python3

"""
This script takes a URL and an email address as command-line arguments,
sends a POST request to the specified URL with the email as a parameter using
the requests package, and displays the body of the response.
"""

import requests
import sys

if len(sys.argv) != 3:
    sys.exit("Usage: ./6-post_email.py <URL> <email>")

url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}
response = requests.post(url, data=data)

print("Your email is:", response.text)
