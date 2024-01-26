#!/usr/bin/python3

"""
This script takes a URL and an email as command-line arguments, sends a POST
request to the specified URL with the email as a parameter, and displays the
body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.parse
import sys

if len(sys.argv) != 3:
    sys.exit("Usage: ./2-post_email.py <URL> <email>")

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')

with urllib.request.urlopen(url, data=data) as response:
    content = response.read().decode('utf-8')
    print(content)
