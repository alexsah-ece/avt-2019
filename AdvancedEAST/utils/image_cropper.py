from PIL import Image


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
    cropped_image.save("./temp/0001_crop.jpg", "JPEG")
