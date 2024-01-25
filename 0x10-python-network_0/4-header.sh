#!/bin/bash
# This script sends a GET request with a custom header to the URL and displays the body of the response

url=$1
response=$(curl -s -H "X-School-User-Id: 98" "$url")
echo "$response"

