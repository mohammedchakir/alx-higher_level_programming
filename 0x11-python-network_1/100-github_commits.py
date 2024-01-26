#!/usr/bin/python3
"""
This script takes the repository name and owner name as command-line arguments,
uses the GitHub API to retrieve the 10 most recent commits from the specified
repository, and prints them in the required format.
"""
import requests
import sys


if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    
    url = "https://api.github.com/repos/{owner_name}/{repository_name}/commits"
    response = requests.get(url)
    commits = response.json()
    try:
        for i in range(10):
            print("{}: {}".format(commits[i].get("sha"),
                                  commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
