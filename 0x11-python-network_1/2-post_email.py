#!/usr/bin/python3

"""Imports a Module"""


import sys
import urllib.parse
import urllib.request


def send_post_request(url, email):
    """creaates a func"""
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))


if __name__ == "__main__":
    send_post_request(sys.argv[1], sys.argv[2])
