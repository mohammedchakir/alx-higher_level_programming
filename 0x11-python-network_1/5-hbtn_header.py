#!/usr/bin/python3

"""
This script takes a URL as a command-line argument, sends a request to the
specified URL using the requests package, and displays the value of the
variable X-Request-Id in the response header.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
