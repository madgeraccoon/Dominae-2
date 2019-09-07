#! /bin/bash
ssh -p 420 evshaddock@elisha.photo "bash -s" < ~/.dominae/sh/remote/sweb.sh && rsync -a --rsh="ssh -p 420" evshaddock@elisha.photo:~/.dominae/out/swebtemp.png ~/.dominae/out/domweb.png