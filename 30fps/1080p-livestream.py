import os

os.system("libcamera-vid --inline --nopreview -t 0 --width 1920 --height 1080 --framerate 30 --codec h264 -o - | ffmpeg -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100 -fflags nobuffer -thread_queue_size 1024 -use_wallclock_as_timestamps 1 -i pipe:0 -c:a aac -preset fast -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/Stream-Key-Here")
