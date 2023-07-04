#!/usr/bin/python3

"""imports a module"""

import requests
import sys


if __name__ == '__main__':
    """main"""
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-ID'))
