#!/usr/bin/python3

"""imports a module"""

import sys
import requests

response = requests.get(sys.argv[1])
print(response.headers.get('X-Request-ID'))
