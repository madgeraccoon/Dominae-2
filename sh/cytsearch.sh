#!/bin/bash
cat /dev/null > ~/.dominae/txt/ytout.txt
youtube-dl --default-search "ytsearch" --get-id "$1" > ~/.dominae/txt/ytout.txt