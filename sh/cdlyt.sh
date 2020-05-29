#!/bin/bash
cat /dev/null > ~/.centipeetle/txt/ytout.txt
youtube-dl -x --audio-format mp3 --default-search "ytsearch" -o '~/.centipeetle/out/ytgrab.%(ext)s' "$1" > ~/.centipeetle/txt/ytout.txt
cat /dev/null > ~/.centipeetle/txt/ytitle.txt
youtube-dl --default-search "ytsearch" -e "$1" > ~/.centipeetle/txt/ytitle.txt