from PIL import Image
import pytesseract
import cv2
import os
import sys
import subprocess
from argparse import ArgumentParser
import numpy as np
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


frame_every = 1     #Extract one frame every this many seconds
score1 = []         #Score of team 1 at each frame
score2 = []         #Score of team 2 at each frame
previous1 = 0       #The most recent successfully detected score of team 1
previous2 = 0       #The most recent successfully detected score of team 2
count=0             #The current frame count
seconds = []        #List with the seconds at which a score change was detected

#Function that parses the command line arguments
def get_args():
    parser = ArgumentParser()
  
    parser.add_argument(
        "--input",
        type=str,
        dest="input"
    )
    parser.add_argument(
        "--ocr",
        type=str,
        dest="ocr"
    )
    
    return parser.parse_args()

#Function that extracts the frames from the input video
def extract_frames(args):
	
    if not os.path.exists('frames/'):
        os.mkdir('frames/')
	
    input_name = args.input.split(os.sep)[-1].split('.')
    command = f"ffmpeg -i {args.input} -vf fps=1/{frame_every} ./frames/{input_name[0]}-frame%04d.jpg"
    command = command.split(' ')
    subprocess.call(command)


#Function that applies OCR to each frame and saves the detected text
def scoreboard_to_txt(img):
    image = cv2.imread(img)
    #cv2.imshow('Colour image', image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    gray = cv2.bitwise_not(gray)

    #Make non score areas completely white after thresholding, hardcoded sadly
    gray[610:675, 340:420]=255
    gray[610:675, 485:555]=255
    gray[610:675, 556:630]=255
    
    #score1 = gray[620:665, 345:480]
    #score2 = gray[620:665, 560:695]

    score = gray[620:665, 345:695]
    
    ret,thresh = cv2.threshold(score,100,255,cv2.THRESH_BINARY)
    #thresh = cv2.GaussianBlur(thresh,(5,5),0)
    #cv2.addWeighted(thresh, 1.5, thresh, -0.5, 0, thresh)

    #cv2.imshow('Thresholded image', thresh)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    # Simple image to string. We keep only the digits of the detected text, which will be the score
    score = pytesseract.image_to_string(thresh, config='digits').split()
    print(score)
    
    if not os.path.exists('score/'):
        os.mkdir('score/')
    dir="score"
    txtname = img.split(os.sep)[-1].split('.')[0]
    #print(dir + os.sep + txtname+".txt")
    
    txt = open(dir + os.sep + txtname+".txt", "w")
    for item in score:
        print(f"{item}", file=txt)
    txt.close()

    update_scoreboard(score)


#Functions which updates the scoreboard and the seconds when a score change was detected. Also checks for erroneous detections
def update_scoreboard(score):
    global count
    global previous1
    global previous2
    if len(score)==2:
        #We assume that the first scoreboard detection is correct (we can make sure of that manually)
        if count==0:
            previous1 = score[0]
            previous2 = score[1]
            score1.append(previous1)
            score2.append(previous2)
        else:
            #If one or both of the scores are more than 3 points away from the previous
            #score, or the previous score is higher than the detected score, it means we have an erroneous detection
            if (abs(int(previous1)-int(score[0])) > 3 or abs(int(previous2)-int(score[1])) > 3 or int(previous1) > int(score[0]) or int(previous2) > int(score[1])):
                score1.append(-1)
                score2.append(-1)   
            else:
                if score[0] != previous1 or score[1] != previous2:
                    seconds.append(frame_every * count)
                    
                previous1 = score[0]
                previous2 = score[1]
                score1.append(previous1)
                score2.append(previous2)

    else:
        score1.append(-1)
        score2.append(-1)
        
    count=count+1
    
#Function that calls scoreboard_to_txt for every extracted frame        
def video_loop(dir):

    images = os.listdir(dir)
    print(images)
    for img in images:
        scoreboard_to_txt(dir + os.sep + img)


#Function that extracts highlights from the input video, according to the seconds when score changes were detected
def extract_highlights(args):
    if not os.path.exists('highlights/'):
        os.mkdir('highlights/')
        
    dir = "highlights"
    target = args.input.split(os.sep)[-1].split('.')[0]
    
    #Extract a highlight for every second when a correct score change was detected
    for sec in seconds:
        ffmpeg_extract_subclip(args.input, sec - 5, sec + 1, targetname = dir + os.sep + f"{target}_{sec}.mp4")


if __name__ == "__main__":

    args=get_args()
    if args.input!=None:
        extract_frames(args)
        
    if args.ocr == "True":
        dir = "frames"
        video_loop(dir)

    print(seconds)
    
    extract_highlights(args)
    
