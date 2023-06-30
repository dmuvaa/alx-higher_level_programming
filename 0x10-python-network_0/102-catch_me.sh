#!/bin/bash
#Bash script that makes a request to on port 5000
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
