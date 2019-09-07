#!/bin/bash
fswebcam -r 1920x1080 --no-banner $HOME/.dominae/out/swebtemp.png -q
magick composite -gravity center $HOME/.dominae/img/overlay.png $HOME/.dominae/out/swebtemp.png $HOME/.dominae/out/sweb.png
rm $HOME/.dominae/out/swebtemp.png