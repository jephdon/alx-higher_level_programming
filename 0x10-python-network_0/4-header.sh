#!/bin/bash
# GET request to a URL with header X-School-User-Id: 98 and displays body
curl -s -H "X-School-User-Id: 98" "$1"
