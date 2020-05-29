#!/bin/bash
convert -size 2000x2000 -channel RGBA -background none -trim -bordercolor none -border 3 -fill '#00A0D4' -font Family-Guy -pointsize 120 caption:"$@" $HOME/.centipeetle/out/cfam.png