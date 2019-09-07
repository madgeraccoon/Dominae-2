#!/bin/bash
cd ~/.dominae/audio/VOX/
sox `xargs -a ~/.dominae/audio/VOX/voxfn.txt`
echo $?