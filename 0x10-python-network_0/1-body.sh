#!/bin/bash
# This script takes a URL, sends a GET request, and displays the body of the response for a 200 status code

url=$1
response=$(curl -s -w "%{http_code}" "$url")

# Check if the status code is 200
if [[ $response == *"200"* ]]; then
    body=$(curl -s "$url")
    echo "$body"
fi

