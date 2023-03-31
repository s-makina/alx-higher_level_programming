#!/usr/bin/python3
"""School staff evaluates candidates
- applying for a back-end position
- with multiple technical challenges,
- like this one:"""
import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Full Name: {data['full_name']}")
        print(f"Description: {data['description']}")
        print(f"Owner: {data['owner']['login']}")
        print(f"Stars: {data['stargazers_count']}")
    else:
        print(f"Error: {response.status_code}")
