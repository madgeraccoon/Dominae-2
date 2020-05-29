#!/bin/bash
convert -size 2000x2000 -channel RGBA -background none -trim -bordercolor none -border 3 -fill "#515622" -font HaloRegular -pointsize 120 caption:"$@" $HOME/.centipeetle/out/chalo.png