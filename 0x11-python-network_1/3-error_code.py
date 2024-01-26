#!/usr/bin/python3

"""
This script takes a URL as a command-line argument, sends a request to the
specified URL, and displays the body of the response (decoded in utf-8).
It also handles urllib.error.HTTPError exceptions and prints the HTTP
status code in case of an error.
"""

import urllib.request
import urllib.error
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: ./3-error_code.py <URL>")

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
        print(content)

except urllib.error.HTTPError as e:
    print("Error code:", e.code)
