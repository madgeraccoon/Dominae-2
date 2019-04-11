#!/bin/bash
cd ~/.centi/VOX/
sox `xargs -a ~/.centi/VOX/voxfn.txt`
echo $?