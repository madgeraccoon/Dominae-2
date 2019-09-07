#! /bin/bash
ssh 192.168.1.4 "bash -s" < ~/.dominae/sh/remote/sfull.sh && rsync -a --rsh="ssh" maddox@192.168.1.4:~/.dominae/out/sfull.png ~/.dominae/out/cremfull.png