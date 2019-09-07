#!/bin/bash
cat /dev/null > ~/.dominae/txt/ytitle.txt
youtube-dl --default-search "ytsearch" -f FORMAT {url1,url2,url3,url4,url5} -e "$1" > ~/.dominae/txt/ytitle.txt
