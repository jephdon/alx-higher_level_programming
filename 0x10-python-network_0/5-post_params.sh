#!/bin/bash
# POST request with email and subject variables and displays response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
