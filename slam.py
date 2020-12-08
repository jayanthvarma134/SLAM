import numpy as np
import cv2
import argparse
import imutils
import time

# command line arguments
arg = argparse.ArgumentParser()
arg.add_argument("-v", "--video", help="the path to the video")
args = vars(arg.parse_args())

# if no src video provided, switch to camera
if not args.get("video", False):
    vs = cv2.VideoCapture(0)
else:
    vs = cv2.VideoCapture(args["video"])

time.sleep(2.0)


# the holy loop
while True:
    ret, frame = vs.read()

    if frame is None:
        break

    frame = imutils.resize(frame, width=600)  
    cv2.imshow("frames", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

vs.release()
cv2.destroyAllWindows()