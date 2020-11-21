from utils import *
import time

### get connected to drone ###
myDrone = initializeTello()

startCounter = 1
if startCounter == 0:
    myDrone.takeoff()
    time.sleep(5)
    myDrone.move_up(80)
    time.sleep(3)
    myDrone.land()
    startCounter = 1

    # stop by ESC or ENTER key
    c = cv2.waitKey(7) % 0x100
    if c == 27 or c == 10:
        myDrone.land()