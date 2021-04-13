# Video FFMPEG

## Configurations - FFMPEG

Add the following lines on configuration file: `configuration.yaml`

```
ffmpeg:
  ffmpeg_bin: /usr/bin/ffmpeg
camera:
  - platform: ffmpeg
    name: camera
    input: rtsp://10.0.12.43:8554/camera

```

## Start stream

Run the following command: `ffmpeg -re -stream_loop -1 -i file.ts -c copy -f rtsp rtsp://10.0.12.43/camera`

## Using VLC

Open vlc as network stream (media) on `udp://@10.0.12.43:1234`