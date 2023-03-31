#!/usr/bin/python3
"""A script that takes your
- GitHub credentials (username and password)
- and uses the GitHub API to display your id"""
import requests
import sys


if __name__ == "__main__":
    # Set up authentication credentials
    username = sys.argv[1]
    password = sys.argv[2]
    auth = (username, password)

    # Make request to GitHub API to get user ID
    url = "https://api.github.com/user"
    response = requests.get(url, auth=auth)

    # Check if request was successful and display user ID
    if response.ok:
        data = response.json()
        print(f"Your user ID is: {data['id']}")
    else:
        print("Failed to get user ID.")
