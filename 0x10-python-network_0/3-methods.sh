#!/bin/bash
# display allowed methods
curl -sI "$1" | awk -F':' '/Allow/{print $2}'
