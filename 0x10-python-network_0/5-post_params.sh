#!/bin/bash
# send post request
curl -sX POST -d "email=test%40gmail.com&subject=I+will+always+be+here+for+PLD" "$1"
