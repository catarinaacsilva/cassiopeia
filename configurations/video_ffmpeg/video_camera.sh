#!/usr/bin/env bash

ffmpeg -stream_loop -1 -i $1 -preset ultrafast -vcodec libx264 -tune zerolatency -b 900k -f mpegts udp://127.0.0.1:1234