import numpy as np
import cv2 as cv



cap = cv.VideoCapture(0)


while True:

    ret, frame = cap.read() #ret is checking if the function works, but if it is i will save the camera output from camera "0" as frame
    width = int(cap.get(3)) #cap.get retrieves information from the capture, in this case the third information which is width
    height = int(cap.get(4)) #and here the 4th, which is height

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_skin = np.array([49, 100, 100])  # Adjust these values
    upper_skin = np.array([109, 255, 255])  # Adjust these values

    mask = cv.inRange(hsv, lower_skin, upper_skin)

    result = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow("Video", result) #Here we create a window which shows the video/image

    if cv.waitKey(1) == ord('q'): #If q is pressed while this is running, break the while loop
        break


cap.release() #make the camera available again
cv.destroyAllWindows() # close all windows









    #light_Red = np.array([[[0, 255, 255]]], dtype=np.uint8)  # Red in BGR
    #dark_Red = np.array([[[0, 0, 123]]], dtype=np.uint8)  # Darker Red in BGR

    # Convert to HSV
    #lower_Red = cv.cvtColor(light_Red, cv.COLOR_BGR2HSV)
    #upper_Red = cv.cvtColor(dark_Red, cv.COLOR_BGR2HSV)

    # Extract and print the H, S, and V components
    #print("Lower Bound (H, S, V):", lower_Red[0][0])
    #print("Upper Bound (H, S, V):", upper_Red[0][0])

    #Lower Bound (H, S, V): [  5  81 190]
    #Upper Bound (H, S, V): [  5  76 200]
