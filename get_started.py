from djitellopy import Tello
import cv2
import time


###########################################################################
width = 320         # width of the image
height = 240        # height of the image
startCounter = 0    # 0 for flight 1 for testing
###########################################################################


# Connect to TELLO
me = Tello()
me.connect()
me.for_back_velocity = 0
me.left_right_velocity = 0
me.up_down_velocity = 0
me.yaw_velocity = 0
me.speed = 0

print(me.get_battery())

me.streamoff()
me.streamon()

while True:

    # get the image from TELLO
    frame_read = me.get_frame_read()
    my_frame = frame_read.frame
    img = cv2.resize(my_frame, (width, height))

    # to go up in the beginning
    if startCounter == 0:
        me.takeoff()
        time.sleep(5)
        # me.move_left(20)
        me.rotate_clockwise(90)
        time.sleep(5)
        me.land()
        startCounter = 1

    # send velocity values to TELLO
    # if me.send_rc_control:
    #     me.send_rc_control(me.left_right_velocity, me.for_back_velocity, me.up_down_velocity, me.yaw_velocity)
    
    # display image
    cv2.imshow("my_result", img)

    # wait for the 'Q' button to stop
    if cv2.waitKey(0) & 0xFF == ord('q'):
        me.land()
        break



