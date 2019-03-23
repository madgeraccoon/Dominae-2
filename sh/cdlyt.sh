#!/bin/bash
cat /dev/null > ~/.dominae/txt/ytout.txt
youtube-dl -x --audio-format mp3 --default-search "ytsearch" -o '~/.dominae/out/ytgrab.%(ext)s' "$1" > ~/.dominae/txt/ytout.txt