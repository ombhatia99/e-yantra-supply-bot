import cv2
import numpy as np
import os

def partA():
    videoFile = "../Videos/RoseBloom.mp4"
    vidcap = cv2.VideoCapture(videoFile)
    success,image = vidcap.read()

    
    seconds = 6
    fps = vidcap.get(cv2.CAP_PROP_FPS) 
    multiplier = fps * seconds

    
    while success:
        frameId = int(round(vidcap.get(1)))
        success, image = vidcap.read()

        if frameId % multiplier == 0:
            cv2.imwrite("../Generated/frame_as_6.jpg",image)
            break

    vidcap.release()
    print ("Complete")


def partB():
    image = cv2.imread("../Videos/frame_as_6.jpg")
    img=image.copy()
    img[:,:,0]=0
    img[:,:,1]=0
    cv2.imwrite('../Generated/frame_as_6_red.jpeg',img)


partA()
partB()
