#!/bin/bash
# script to display all the http methods the server will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
