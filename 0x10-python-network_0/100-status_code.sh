#!/bin/bash
#Write a Bash script that sends a request to a URL passed as an argument
curl -s -o /dev/null -w "%{http_code}" "$1"
