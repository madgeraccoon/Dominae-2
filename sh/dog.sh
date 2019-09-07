#!/bin/bash
GIVEDOG=`curl https://random.dog/woof 2>/dev/null`
printf "https://random.dog/$GIVEDOG" > $HOME/.dominae/txt/give.txt