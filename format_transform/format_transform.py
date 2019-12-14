from PyQt5.QtGui import QImage
import os

from yolo_io import YoloReader, YOLOWriter
from pascal_voc_io import PascalVocWriter, PascalVocReader
from argparse import ArgumentParser


class FormatTransform:

    def __init__(self, data_folder):
        self.data_folder = data_folder
        self.files_created = 0

    @staticmethod
    def convertPoints2BndBox(points):
        xmin = float('inf')
        ymin = float('inf')
        xmax = float('-inf')
        ymax = float('-inf')
        for p in points:
            x = p[0]
            y = p[1]
            xmin = min(x, xmin)
            ymin = min(y, ymin)
            xmax = max(x, xmax)
            ymax = max(y, ymax)

        # Martin Kersner, 2015/11/12
        # 0-valued coordinates of BB caused an error while
        # training faster-rcnn object detector.
        if xmin < 1:
            xmin = 1

        if ymin < 1:
            ymin = 1

        return (int(xmin), int(ymin), int(xmax), int(ymax))

    def _transform_single_file(self, Reader, Writer, image_path, is_image_needed):

        # load image into memory
        image = QImage()
        image.load(image_path)
        imgSize = [image.height(), image.width(),
                        1 if image.isGrayscale() else 3]

        # parse input format
        try:
            # discard extension from file name and append the extension
            # of the format to transform
            input_file = image_path.split('.')[0] + Reader.FILE_EXT
            if (is_image_needed):   
                reader = Reader(input_file, image)
            else:
                reader = Reader(input_file)
            shapes = reader.getShapes()
        except FileNotFoundError:
            print(f"No {Reader.FILE_EXT} file found, skipping for {image_path} ...")
            return
        
        # initialize Writer object to prepare for .xml file creation
        writer = Writer(
            foldername=image_path.split('/')[-2],
            filename=image_path.split('/')[-1],
            imgSize=imgSize,
            localImgPath=image_path
        )

        # insert fields extracted from reader to writer
        for shape in shapes:
            points = shape[1]
            label = shape[0]
            difficult = 0
            bndbox = FormatTransform.convertPoints2BndBox(points)
            writer.addBndBox(bndbox[0], bndbox[1], bndbox[2], bndbox[3], label, difficult)

        # store output format 
        writer.save()
        self.files_created += 1

    def _single_yolo_to_voc(self, image_path):
        self._transform_single_file(YoloReader, PascalVocWriter, image_path, True)

    def _single_voc_to_yolo(self, image_path):
        self._transform_single_file(PascalVocReader, YOLOWriter, image_path, False)

    def yolo_to_voc(self):
        self._transform_files(self._single_yolo_to_voc)

    def voc_to_yolo(self):
        self._transform_files(self._single_voc_to_yolo)

    def _transform_files(self, transform_function):
        for file in os.listdir(self.data_folder):
            if file.endswith(".jpg"):
                filepath = os.path.join(self.data_folder, file)
                transform_function(os.path.abspath(filepath))

        print(f"Operation finished, {self.files_created} files were created")

def get_args():
    parser = ArgumentParser()
    parser.add_argument(
        "dir",
        type=str,
        help="Directory of the dataset where the format transformation will take place"
    )
    parser.add_argument(
        "mode",
        type=str,
        choices=['yolo_to_voc','voc_to_yolo'],
        help="Choose the kind of transformation to take place"
    )
    
    return parser.parse_args()

if "__name__==__main__":

    args = get_args()

    ft = FormatTransform(args.dir)
    
    if(args.mode == "yolo_to_voc"):
        ft.yolo_to_voc()
    else:
        ft.voc_to_yolo()



