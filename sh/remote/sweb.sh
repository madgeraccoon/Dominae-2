#!/bin/bash
fswebcam -r 1920x1080 -S 20 --no-banner $HOME/.dominae/out/swebtemp.png -q
magick composite -gravity southeast $HOME/.dominae/img/overlay2.png $HOME/.dominae/out/swebtemp.png $HOME/.dominae/out/sweb.png