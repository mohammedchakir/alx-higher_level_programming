#!/bin/bash
# This script takes a URL and displays all HTTP methods the server will accept

url=$1
allowed_methods=$(curl -sI -X OPTIONS "$url" | grep -i "Allow" | awk '{print $2}')
echo "$allowed_methods"

