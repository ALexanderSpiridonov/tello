from utils import *
import cv2
import time

w, h = 360, 240
pid = [0.5, 0.5, 0]
pError = 0
startCounter = 0 # for testing should be 1 (no Flight mode)

### get connected to drone ###
myDrone = initializeTello()

while True:
    ## Flight
    if startCounter == 0:
        myDrone.takeoff()
        time.sleep(5)
        myDrone.move_up(120)
        time.sleep(5)
        startCounter = 1

    ## Step 1
    img = telloGetFrame(myDrone, w, h)

    ## Step 2
    img, info = findFace(img)
    # print x coordinate for center
    print(info[0][0]) 

    ## Step 3
    pError = trackFace(myDrone, info, w, pid, pError)

    cv2.imshow('Image', img)
    # stop by q (doesnt work)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    
    # stop by ESC or ENTER key
    c = cv2.waitKey(7) % 0x100
    if c == 27 or c == 10:
        myDrone.land()
        break