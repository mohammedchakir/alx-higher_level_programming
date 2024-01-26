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


if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
