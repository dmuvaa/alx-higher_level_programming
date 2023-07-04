#!/usr/bin/python3

"""imports a module"""

import requests
import sys


if __name__ = '__main__':
    """main"""
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.text)
