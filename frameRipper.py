import cv2
import os

cap = input("Insert video file here")
# Read the video on opencv and save frames to images directory
cap = cv2.VideoCapture(cap)
fps = int(cap.get(5))
#fps = 35
print(fps)
i=0
#os.system("mkdir danceVideos")
directory = "robosBallsPicsTrain"
x = 0
y = 1362
while(cap.isOpened()):
    # Read the frames and while there are new frames save them starting at image1.jpg to however many frames there are
    ret, frame = cap.read()
    if ret == False:
        break
    if x == 50:
    	cv2.imwrite(os.path.join(directory,"image"+str(y)+'.jpg'),frame)
    	x = 0
    	y+=1
    x+=1
    i+=1
# Clean up when there are no more new frames
cap.release()

