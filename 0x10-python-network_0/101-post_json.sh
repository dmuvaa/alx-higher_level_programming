#!/bin/bash
#Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
curl -X POST -H "Content-Type: application/json" -d @req.json http://localhost:9500
