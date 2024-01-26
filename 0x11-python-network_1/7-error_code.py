#!/usr/bin/python3

"""
This script takes a URL as a command-line argument, sends a request to the
specified URL using the requests package, and displays the body of the
response. If the HTTP status code is greater than or equal to 400,
it prints an error message with the value of the HTTP status code.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

if response.status_code >= 400:
    print("Error code:", response.status_code)
else:
    print(response.text)
