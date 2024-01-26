#!/usr/bin/python3

"""
This script takes a letter as a command-line argument, sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter using the
requests package, and processes the JSON response accordingly.
"""
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    lett = "" if len(sys.argv) == 1 else sys.argv[1]
    data = {"q": lett}

    response = requests.post(url, data=data)

    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
