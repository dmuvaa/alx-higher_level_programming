#!/usr/bin/python3

"""Imports a Module"""

import urllib.request
import sys


def get_request_id('https://alx-intranet.hbtn.io'):
    with urllib.request.urlopen('https://alx-intranet.hbtn.io') as response:
        print(response.headers.get('X-Request-Id'))


def main():
    url = sys.argv[1]
    get_request_id('https://alx-intranet.hbtn.io')


if __name__ == "__main__":
    main()
