#!/bin/bash
convert -size 2000x2000 -channel RGBA -background none -trim -bordercolor none -border 3 -fill '#29cc71' -font Crewniverse -pointsize 120 caption:"$@" $HOME/.dominae/out/ssay.png
