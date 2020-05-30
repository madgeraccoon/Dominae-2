#!/bin/bash
args="$@"
API=`cat $HOME/.centipeetle/txt/ytapi` 
curl 'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q='"$args"'&type=video&key='"$API" | jq -r '.items[].id.videoId, .items[].snippet.title' > ~/.centipeetle/txt/ytout.txt
