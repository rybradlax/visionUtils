import cv2
import numpy as np
global imagen
import time
#from picamera.array import PiRGBArray
#from picamera import PiCamera
#camera = PiCamera()
##1440,1140
#camera.resolution = (800,600)  
#camera.framerate = 32
#rawCapture = PiRGBArray(camera, size=(800,600))
time.sleep(0.1)
x1 = 0
x2 = 0
y1 = 0
y2 = 0
count = 0
imagen=cv2.imread(r"C:\Users\rjpea\OneDrive\Pictures\Screenshots\NoTouchOrders_Name_Small.png")
def evento_mouse(event, x, y, flags, param):
    global count
    global x1,y1

    global x2,y2

    if event == cv2.EVENT_FLAG_LBUTTON and count==0:
        print ('Corner 1 selected...Click corner 2')
        height = y
        width = x
        print(x,y)

        x1 = x
        y1 = y
        count = 1
        time.sleep(.1)
        #test()
        #print 'hello'
    elif event == cv2.EVENT_FLAG_LBUTTON and count==1:
        print ('Corner 2 selected.  Click again to create another box.')
        height = y
        width = x
        x2 = x
        y2 = y
        count = 0
        makeBox(y1,y2,x1,x2)
        #test()
        #print 'hello'
    
        
#def test():
    #global x1, y1
#    print x1
#    print y1

def makeBox(y1,y2,x1,x2):
    try:
        global imagen
        roi=imagen[y1:y2,x1:x2] 
        hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
        #print(hsv)
        #imagen[y1:y2,x1:x2] = (0,0,255)
        hsv2=np.mean(hsv, axis=0)
        print('Average value:'+str(np.mean(hsv2, axis=0)))
        print('Min value    :'+str(np.min(hsv2, axis=0)))
        print('Max Valuu    :'+str(np.max(hsv2, axis=0)))
    except:
        pass
#camera.capture('/home/pi/Desktop/image.jpg')

cv2.imshow('image.jpg',imagen)
cv2.setMouseCallback('image.jpg',evento_mouse)
cv2.waitKey(0) 
cv2.destroyAllWindows()
