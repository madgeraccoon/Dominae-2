#!/bin/bash
ssh 192.168.1.7 "bash -s" < ~/.dominae/sh/remote/cfetch.sh && rsync -a --rsh="ssh" maddox@192.168.1.7:~/.dominae/txt/screenfetch.txt ~/.dominae/txt/cremfetch.txt
sed -i -e 's/^/**/' ~/.dominae/txt/screenfetch.txt
sed -i -e 's/:/**:/' ~/.dominae/txt/screenfetch.txt
sed -i -e 's/@/**@/g' ~/.dominae/txt/screenfetch.txt
sed -i -e 's/**@ /@ /g' ~/.dominae/txt/screenfetch.txt
#sed -i -e 's/**@**/@/g' ~/.dominae/txt/screenfetch.txt
