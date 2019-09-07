#! /bin/bash
ssh 192.168.1.4 "bash -s" < ~/.dominae/sh/remote/swindow.sh && rsync -a --rsh="ssh" maddox@192.168.1.4:~/.dominae/out/swindow.png ~/.dominae/out/cremwindow.png