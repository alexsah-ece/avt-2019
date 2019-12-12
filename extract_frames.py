import ffmpeg
import sys
# ffmpeg -i iowa.mp4 -ss 00:09:13.200 -vframes 20 thumb%04d.jpg -hide_banner

# argv[1] is filename for extraction
# argv[2] is starting timestamp in format hh:mm:ss.msc 
# argv[3] is ending timestamp, same format as argv[2]

# ffmpeg -i movie.mp4 -ss 00:00:03 -t 00:00:08 -async 1 -c copy cut.mp4 

filename = sys.argv[1]
start_time = sys.argv[2]
end_time = sys.argv[3]

