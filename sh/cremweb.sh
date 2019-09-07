#! /bin/bash
ssh maddox@192.168.1.7 "bash -s" < ~/.dominae/sh/remote/sweb.sh && rsync -a --rsh="ssh" maddox@192.168.1.7:~/.dominae/out/swebtemp.png ~/.dominae/out/cremweb.png