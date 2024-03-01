#!/bin/bash
# display status code
curl -sw "%{http_code}" -o /dev/null "$1" # curl -sI "$1" | awk '/HTTP\/1.1/ {print $2}' | tr -d '\n'
