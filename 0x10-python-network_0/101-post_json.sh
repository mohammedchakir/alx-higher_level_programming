#!/bin/bash
# This script sends a JSON POST request to a URL and displays the body of the response
# Send POST request with JSON content
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
