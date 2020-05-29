#!/bin/bash
fswebcam --set "White Balance Temperature, Auto"="False" --set "Gamma"="72" --set "Contrast"="32" --set "Power Line Frequency"="60 Hz" --set "Backlight Compensation"="0" --set "White Balance Temperature"="4500" --set "Exposure, Auto"="Manual Mode" --set "Exposure (Absolute)"="450" --set "Exposure, Auto Priority"="False" -r 1920x1080 -p MJPEG -D 1 --no-banner $HOME/.centipeetle/out/swebtemp.png -q --verbose
#fswebcam -r 1920x1080 -p MJPEG -D 1 --no-banner $HOME/.centipeetle/out/swebtemp.png -q
magick composite -gravity center -blend 50 $HOME/.centipeetle/img/overlay.png $HOME/.centipeetle/out/swebtemp.png $HOME/.centipeetle/out/sweb.png
rm $HOME/.centipeetle/out/swebtemp.png