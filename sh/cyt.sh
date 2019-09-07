#!/bin/bash
args="$@"
curl 'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q='"$args"'&type=video&key=AIzaSyCSqOqZJXTlu2DJ8s1ngQfHrtR4enhvhH0' | jq -r '.items[].id.videoId, .items[].snippet.title' > ~/.dominae/txt/ytout.txt