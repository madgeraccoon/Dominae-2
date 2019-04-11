#!/bin/bash
cat /dev/null > ~/.dominae/txt/ytout.txt
youtube-dl -x --audio-format mp3 --default-search "ytsearch" -o '~/.dominae/out/ytgrab.%(ext)s' "$1" > ~/.dominae/txt/ytout.txt
cat /dev/null > ~/.dominae/txt/ytitle.txt
youtube-dl --default-search "ytsearch" -e "$1" > ~/.dominae/txt/ytitle.txt