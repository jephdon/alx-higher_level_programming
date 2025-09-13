#!/bin/bash
# Displays all HTTP methods the server accepts for a given URL
curl -s -I -X OPTIONS "$1" | grep -i "^Allow:" | cut -d' ' -f2-
