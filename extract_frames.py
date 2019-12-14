import sys
import subprocess
import os
from argparse import ArgumentParser


def initiate_extraction():
    args = get_args()
    validate_args(args)
    extract_frames(args)


def get_args():
    parser = ArgumentParser()
    parser.add_argument(
        "--start",
        type=str,
        dest="start",
        required=True
    )
    parser.add_argument(
        "--end",
        type=str,
        dest="end",
        required=True
    )
    parser.add_argument(
        "input",
        type=str,
        default="."
    )
    parser.add_argument(
        "--fps",
        type=str,
        default="25"
    )
    return parser.parse_args()


def validate_args(args):
    # Check if the provided arguments have the correct format
    time_argument_validation(args.start)
    time_argument_validation(args.end)


def time_argument_validation(time_arg):
    splitted_arg = time_arg.split(':')
    if (len(splitted_arg) != 3):
        raise Exception('--start and --end must follow format hh:mm:ss')

    for arg in splitted_arg:
        if (len(arg) != 2 or int(arg[0]) >= 6):
            raise Exception(
                'each of --start and --end arguments must be in range [00,59]')


def extract_frames(args):
    if not os.path.exists('frames/'):
        os.mkdir('frames/')

    input_name = args.input.split('/')[-1].split('.')
    command = f'ffmpeg -i {args.input} -vf fps={args.fps} -ss {args.start} -to {args.end} ./frames/{input_name[0]}-frame%04d.jpg'
    command = command.split(' ')
    subprocess.call(command)


if "__name__==__main__":
    initiate_extraction()
