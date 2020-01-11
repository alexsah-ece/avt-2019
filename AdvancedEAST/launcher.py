from utils.process_image import process_image
from PIL import Image
from utils.frame_extract import extract_frame_per_second
from predict import start_prediction


if __name__ == "__main__":
    for filename, index in extract_frame_per_second("./video.mp4"):
        frame = Image.open(filename)
        processed = process_image(frame)
        processed_filename = "./cropped/" + str(index) + ".jpeg"
        processed.save(processed_filename, "JPEG")
        start_prediction(processed_filename)


    print("Done.")
