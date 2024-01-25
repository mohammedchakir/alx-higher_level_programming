#!/bin/bash
# This script takes a URL, sends a request, and displays the size of the response body in bytes

url=$1
size=$(curl -sI "$url" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r')
echo "$size"

