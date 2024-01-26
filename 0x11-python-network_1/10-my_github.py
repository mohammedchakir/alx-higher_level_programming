#!/usr/bin/python3

"""
This script takes GitHub credentials (username and personal access token) as
command-line arguments, uses Basic Authentication with the GitHub API to
display the user's ID.
"""
from requests.auth import HTTPBasicAuth
import requests
import sys


if __name__ == "__main__":
    authen = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=authen)
    print(response.json().get("id"))
