#!/bin/bash
DISPLAY=:0 scrot -u $HOME/.dominae/out/swindowtemp.png -d 3
magick composite -gravity southeast $HOME/.dominae/img/overlay2.png $HOME/.dominae/out/swindowtemp.png $HOME/.dominae/out/swindow.png