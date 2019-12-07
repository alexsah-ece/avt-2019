# Documentation

## Setup
_Python 3 is assumed to be the version of python in use._

To install the required packages run:
```
pip install requirements.txt
```

## Video download & Crop

### Video Download
To download a video from youtube you have to:
- Create a `videos` folder 
- Create a `links.txt` file containing the videos you want to download
- Run `python custom_video.py`

The videos will be downloaded into the `videos` directory.

### Video Crop
To crop an already downloaded video you can run:
```
python crop-video.py {VIDEO_TO_CROP} \
    -o {CROPPED_VIDEO} \
    --start {START_TIME_IN_SECONDS} \
    --end 20 {END_TIME_IN_SECONDS}
```
Example - Crop video and retain the part between 5-15 seconds, saving its output to `mydata/cropped.mp4`:
```
python crop-video.py videos/full_video.mkv \
    -o videos/cropped.mkv \
    --start 5 \
    --end 15
```