#!/usr/bin/python3

"""
This script takes a URL and an email as command-line arguments, sends a POST
request to the specified URL with the email as a parameter, and displays the
body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

 request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
