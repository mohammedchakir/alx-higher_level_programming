#!/usr/bin/python3
"""
Uses the GitHub API to retrieve and display a GitHub user ID based on given credentials.
Usage: ./github_user_id.py <GitHub username> <GitHub password>
  - Utilizes Basic Authentication to access the user ID.
"""
import sys
import requests

def get_github_user_id(username, password):
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        return response.json().get("id")
    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./github_user_id.py <GitHub username> <GitHub password>")
    else:
        github_username, github_password = sys.argv[1], sys.argv[2]
        user_id = get_github_user_id(github_username, github_password)

        if user_id is not None:
            print(f"GitHub User ID: {user_id}")
        else:
            print("Failed to retrieve GitHub User ID.")

