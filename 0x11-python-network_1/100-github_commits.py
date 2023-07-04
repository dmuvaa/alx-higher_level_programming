#!/usr/bin/python3

"""imports a module"""

import requests
from sys import argv


if __name__ == "__main__":
    """main"""
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    response = requests.get(url)
    commits = response.json()
    for commit in commits[:10]:
        print(commit.get("sha"), end=": ")
        print(commit.get('commit').get('author').get('name'))
