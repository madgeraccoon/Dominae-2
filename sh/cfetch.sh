#!/bin/bash

screenfetch -N -n > ~/.centipeetle/txt/screenfetch.txt
sed -i -e 's/^/**/' ~/.centipeetle/txt/screenfetch.txt
sed -i -e 's/:/**:/' ~/.centipeetle/txt/screenfetch.txt
sed -i -e 's/@/**@/g' ~/.centipeetle/txt/screenfetch.txt
sed -i -e 's/**@ /@ /g' ~/.centipeetle/txt/screenfetch.txt
#sed -i -e 's/**@**/@/g' ~/.centipeetle/txt/screenfetch.txt
