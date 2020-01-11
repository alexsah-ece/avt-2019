from utils.image_cropper import crop_bottom_third
from PIL import Image
from utils.frame_extract import extract_frame_per_second
from predict import start_prediction


if __name__ == "__main__":
    for filename, index in extract_frame_per_second("./video.mp4"):
        frame = Image.open(filename)
        cropped = crop_bottom_third(frame)
        cropped_filename = "./cropped/" + str(index) + ".jpeg"
        cropped.save(cropped_filename, "JPEG")
        start_prediction(cropped_filename)

    print("Done.")
