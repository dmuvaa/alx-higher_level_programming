#!/usr/bin/python3

"""imports a module"""

import requests
import sys

if len(sys.argv) == 2:
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
