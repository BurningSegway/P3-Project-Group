import numpy as np
import cv2 as cv



cap = cv.VideoCapture(0)


while True:
    ret, frame = cap.read() #ret is checking if the function works, but if it is i will save the camera output from camera "0" as frame
    width = int(cap.get(3)) #cap.get retrieves information from the capture, in this case the third information which is width
    height = int(cap.get(4)) #and here the 4th, which is height


    image = np.zeros(frame.shape, np.uint8) # this function simply creates and all black image the same size as our frame
    smallerImage = cv.resize(frame, (0,0), fx=0.5, fy=0.5) #Here we resize that smaller image to be half the size
    image[ :height//2, :width//2] = cv.rotate(smallerImage, cv.ROTATE_180) #This determines what image/video should be placed where, here we rotate the image/video we are placing in the top left corner
    image[ :height//2, width//2:] = cv.rotate(smallerImage, cv.ROTATE_180) 
    image[ height//2:, :width//2] = smallerImage
    image[ height//2:, width//2:] = smallerImage

    cv.imshow("Video", image) #Here we create a window which shows the video/image

    if cv.waitKey(1) == ord('q'): #If q is pressed while this is running, break the while loop
        break


cap.release() #make the camera available again
cv.destroyAllWindows() # close all windows



