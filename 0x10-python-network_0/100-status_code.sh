#!/bin/bash
# display status code
curl -s -o /dev/null -I --w "%{http_code}" "$1" 
