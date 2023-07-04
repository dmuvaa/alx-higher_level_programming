#!/usr/bin/python3

"""Imports a Module"""

import urllib.request
import sys


def get_request_id(url):
    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))


def main():
    url = sys.argv[1]
    get_request_id(url)


if __name__ == "__main__":
    main()
