#!/bin/bash
# catch me
curl -sLX PUT -d  "user_id=98" -H "Origin: School" -e 0.0.0.0:5000/catch_me 0.0.0.0:5000/catch_me_2
