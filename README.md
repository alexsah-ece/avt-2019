# Documentation

## Setup
_Python 3 is assumed to be the version of python in use._

To install the required packages run:
```
pip install -r requirements.txt
```

Add ffmpeg with
```
sudo apt-get install ffmpeg
```
## Video download & Crop

### Video Download
To download a video from youtube you have to:
- Create a `videos` folder 
- Create a `links.txt` file containing the videos you want to download
- Run `python download_video.py`

The videos will be downloaded into the `videos` directory.

### Video Crop
To crop an already downloaded video you can run:
```shell
python crop_video.py {VIDEO_TO_CROP} \
    -o {CROPPED_VIDEO} \
    --start {START_TIME_IN_SECONDS} \
    --end 20 {END_TIME_IN_SECONDS}
```
Example - Crop video and retain the part between 5-15 seconds, saving its output to `mydata/cropped.mp4`:
```shell
python crop_video.py videos/full_video.mkv \
    -o videos/cropped.mkv \
    --start 5 \
    --end 15
```

### Frames extraction
To extract frames from an already downloaded video you can run
```shell
    python extract_frames.py {PATH_TO_VIDEO} --start {START_TIME in format hh:mm:ss} --end {END_TIME in format hh:mm:ss}
```
Example - Extract frames from 1'25" to 1'49"
```shell
python extract_frames.py videos/76ers_vs_nuggets_dec2019.mp4 --start 00:01:25 --end 00:01:49
```
