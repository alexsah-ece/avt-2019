import cv2
import math


def extract_frame_per_second(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_rate = cap.get(5)  # frame rate
    x = 1
    while cap.isOpened():
        frame_id = cap.get(1)  # current frame number
        ret, frame = cap.read()
        if not ret:
            break
        if frame_id % math.floor(frame_rate) == 0:
            filename = './frames/image.jpeg'
            cv2.imwrite(filename, frame)
            yield filename, x
            x += 1
    cap.release()


if __name__ == "__main__":
    videoFile = "video.mp4"
    for i in extract_frame_per_second(videoFile):
        print(i)
    print("Done!")



