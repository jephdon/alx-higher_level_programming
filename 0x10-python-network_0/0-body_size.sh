#!/bin/bash
# Sends a request to a URL and displays the size of the response body in bytes
curl -s -w "%{size_download}" "$1" -o /dev/null
