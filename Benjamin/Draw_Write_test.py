import numpy as np
import cv2 as cv



cap = cv.VideoCapture(0)


while True:
    ret, frame = cap.read() #ret is checking if the function works, but if it is i will save the camera output from camera "0" as frame
    width = int(cap.get(3)) #cap.get retrieves information from the capture, in this case the third information which is width
    height = int(cap.get(4)) #and here the 4th, which is height

    #Here are the functions to draw lines, circles, rectangles, and text on an image/video
    #above each unique row will be the function params to the side more explanation if neededs

    #The line (Canvas, Line start, Line end, Color, thickness)
    img = cv.line(frame, (0,0), (width,height), (0, 0, 255), 1) 
    img = cv.line(img, (width,0), (0,height), (100, 100, 100), 1)#Here we switch to drawing on the precious image as the new canvas to keep the precious drawings

    #The rectangle (Canvas, rectangle corner 1, rectangle corner 2, Color, thickness)
    img = cv.rectangle(img, (5,5), (200,200), (0, 0, 255), 1)
    img = cv.rectangle(img, (30,30), (175,175), (0, 0, 255), -1) #-1 in thicknees fills out the given shape

    #The Circle (Canvas, Centerpoint, Radius, Color, thickness)
    img = cv.circle(img, (width//2,height//2), 60, (0, 0, 255), 1)


    font = cv.FONT_HERSHEY_COMPLEX #Just saving a random font type as a variable
    #Text (Canvas, TEXT, placement, Font, Font size, Color, thickness, weird shit that makes "Text look better")
    img = cv.putText(img, 'Easy cunts', (width//2, height - 10), font, 1, (0, 0, 0), 2, cv.LINE_AA)


    cv.imshow("Video", img) #Here we create a window which shows the video/image

    if cv.waitKey(1) == ord('q'): #If q is pressed while this is running, break the while loop
        break


cap.release() #make the camera available again
cv.destroyAllWindows() # close all windows
