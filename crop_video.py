from argparse import ArgumentParser
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def get_args():
    parser = ArgumentParser()
    parser.add_argument(
        "--start",
        type=float,
        dest="start",
        required=True
    )
    parser.add_argument(
        "--end",
        type=float,
        dest="end",
        required=True
    )
    parser.add_argument(
        "input",
        type=str,
        default="."
    )
    parser.add_argument(
        "-o",
        type=str,
        dest="output",
        default="."
    )
    return parser.parse_args()

if "__name__==__main__":
    args = get_args()
    ffmpeg_extract_subclip(args.input, args.start, args.end, targetname=args.output)
