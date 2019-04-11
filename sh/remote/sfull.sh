#!/bin/bash
DISPLAY=:0 scrot ~/.dominae/out/sfulltemp.png
magick composite -gravity southeast $HOME/.dominae/img/overlay2.png $HOME/.dominae/out/sfulltemp.png $HOME/.dominae/out/sfull.png