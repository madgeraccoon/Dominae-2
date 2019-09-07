#!/bin/bash
GIVECAT=`curl https://loremflickr.com/json/512/512/$@/all 2>/dev/null | jq -r '.file'`
printf "$GIVECAT" > $HOME/.dominae/txt/give.txt