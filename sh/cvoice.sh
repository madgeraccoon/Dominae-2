#!/bin/bash
VIDEO=`youtube-dl -x --audio-format mp3 -o '~/.dominae/out/ytgrab.%(ext)s' "$1"`