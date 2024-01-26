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
    json_data = response.json()
    if json_data:
        print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
    else:
        print("No result")

except ValueError:
    print("Not a valid JSON")
