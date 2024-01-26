#!/usr/bin/python3
"""
This script takes the repository name and owner name as command-line arguments,
uses the GitHub API to retrieve the 10 most recent commits from the specified
repository, and prints them in the required format.
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])
    response = requests.get(url)
    commits = response.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
