#!/bin/bash
cd ~/.dominae/animalese/
sox `xargs -a ~/.dominae/animalese/voxfn.txt` canimal.wav speed 1.55
echo $?