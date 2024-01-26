#!/usr/bin/python3

"""
This script takes the repository name and owner name as command-line arguments,
uses the GitHub API to retrieve the 10 most recent commits from the specified
repository, and prints them in the required format.
"""

import requests
import sys

if len(sys.argv) != 3:
    sys.exit("Usage: ./100-github_commits.py <repository_name> <owner_name>")

repository_name = sys.argv[1]
owner_name = sys.argv[2]

url = f'https://api.github.com/repos/{owner_name}/{repository_name}/commits'
params = {'per_page': 10}
response = requests.get(url, params=params)

commits = response.json()

for commit in commits:
    sha = commit.get('sha')
    author_name = commit.get('commit').get('author').get('name')
    print(f'{sha}: {author_name}')
