#!/bin/bash
args="$@"
echo "This is a placeholder so that the youtube results have the proper numbers" > ~/.centipeetle/txt/ytsout.txt
API=`cat $HOME/.centipeetle/txt/ytapi` 
curl 'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=5&q='"$args"'&type=video&key='"$API" | jq -r '.items[].id.videoId, .items[].snippet.title' >> ~/.centipeetle/txt/ytsout.txt
