#!/bin/bash
# This script sends a POST request with parameters to the URL and displays the body of the response

url=$1
email="test@gmail.com"
subject="I will always be here for PLD"

response=$(curl -s -X POST -d "email=$email&subject=$subject" "$url")
echo "$response"

