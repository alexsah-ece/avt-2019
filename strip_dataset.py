import os
from argparse import ArgumentParser

def get_args():
    parser = ArgumentParser()
    parser.add_argument(
        "dir",
        type=str,
        help="Directory of the dataset where the format transformation will take place"
    )
    return parser.parse_args()

if "__name__ == __main__":
    
    args = get_args()

    files = os.listdir(args.dir)
    files_to_remove = []
    for file in files:
        if file.endswith(".jpg"):
            # remove jpg extension
            prefix = file.split('.')[0]
            # find respective .xml .txt files
            xml = prefix + ".xml"
            txt = prefix + ".txt"
            print(prefix, xml, txt)
            if (xml not in files) and (txt not in files):
                files_to_remove.append(file)
    print(files_to_remove)
    for f in files_to_remove:
        rel_path = os.path.join(args.dir, f)
        abs_path = os.path.abspath(rel_path)
        os.remove(abs_path)