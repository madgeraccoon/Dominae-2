#!/bin/bash
convert -size 2000x2000 -channel RGBA -background none -trim -bordercolor none -border 3 -fill "#cec8c8" -font Minecrafter-Alt -pointsize 120 caption:"$@" $HOME/.centipeetle/out/ccraft.png