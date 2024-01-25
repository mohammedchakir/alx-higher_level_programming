#!/bin/bash
# This script sends a JSON POST request to a URL and displays the body of the response

url=$1
json_file=$2

# Check if the file exists and is readable
if [ ! -r "$json_file" ]; then
    echo "File not found or not readable: $json_file"
    exit 1
fi

# Check if the file contains valid JSON
if ! jq . "$json_file" &> /dev/null; then
    echo "Not a valid JSON: $json_file"
    exit 1
fi

# Send POST request with JSON content
response=$(curl -s -X POST -H "Content-Type: application/json" -d @"$json_file" "$url")
echo "$response"

