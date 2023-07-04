#!/usr/bin/python3

"""Imports a Module"""


import sys
import urllib.request
import urllib.error


def send_request(url):
    """python script that takes a url"""
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    """main"""
    send_request(sys.argv[1])
