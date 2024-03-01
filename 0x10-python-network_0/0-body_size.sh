#!/bin/bash
# use curl to send request to display size of response body
curl -sI "$1" | awk '/Content-Length: / {print $2}' 
