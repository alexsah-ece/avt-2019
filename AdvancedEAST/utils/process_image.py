from PIL import Image


def process_image(img_file, bw_thresh=150):
    cropped = crop_bottom_third(img_file)
    bw = convert_black_and_white(cropped)
    return bw


def convert_black_and_white(img_file, bw_thresh=150):
    # img_file: An image object opened by Pillow
    # bw_thresh: The conversion threshold
    # The default value is enough for most cases but if the scoreboard background is too light, you should pass
    # a higher value
    fn = lambda x: 255 if x > bw_thresh else 0
    bw = img_file.convert('L').point(fn, mode='1')
    return bw


def crop_bottom_third(image_to_crop):
    width, height = image_to_crop.size  # Get dimensions
    left = 0
    top = 2 * height / 3
    right = width
    bottom = height
    cropped = image_to_crop.crop((left, top, right, bottom))
    return cropped


if __name__ == "__main__":
    test_image = "./temp/0001.jpg"
    image = Image.open(test_image)
    cropped_image = crop_bottom_third(image)
    thresh = 0
    fn = lambda x: 255 if x > thresh else 0
    r = cropped_image.convert('L').point(fn, mode='1')
    r.save("./temp/a2.jpg", "JPEG")
