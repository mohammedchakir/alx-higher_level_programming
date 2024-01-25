#!/bin/bash
# This script sends a DELETE request to the URL and displays the body of the response

url=$1
response=$(curl -s -X DELETE "$url")
echo "$response"

