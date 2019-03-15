#!/bin/bash
ffmpeg -f pulse -ac 2 -i default -f v4l2 -framerate 60 -video_size 1920x1080 -input_format mjpeg -i /dev/video0 -preset faster -pix_fmt yuv420p -t 00:00:15  $HOME/.dominae/img/out.mkv -y -loglevel panic
ffmpeg -i $HOME/.dominae/img/out.mkv -itsoffset 1.2 -i $HOME/.dominae/img/out.mkv -vcodec copy -acodec copy -map 0:1 -map 1:0 $HOME/.dominae/img/outs.mkv -y -loglevel panic
ffmpeg -i $HOME/.dominae/out/outs.mkv -b 1000000 $HOME/.dominae/out/smov.webm -y -loglevel panic