import numpy as np
import cv2 as cv



cap = cv.VideoCapture(0)

size = 500
x=0
print('program initiation')
while True:
    ret, frame = cap.read() #ret is checking if the function works, but if it is i will save the camera output from camera "0" as frame
    width = int(cap.get(3)) #cap.get retrieves information from the capture, in this case the third information which is width
    height = int(cap.get(4)) #and here the 4th, which is height
    video_RS = cv.resize(frame, (size, size)) #Resize image
    
    
    
    pixel_bgr = video_RS[size//2][size//2] #Choose the middel pixel
    
    pixel_bgr_Array = np.array(pixel_bgr)  # seyup array for the pixel

    # Convert the chosen color to RGB
    pixel_rgb = cv.cvtColor(np.uint8([[pixel_bgr_Array]]), cv.COLOR_BGR2RGB)[0][0]

    # Convert the chosen color to HSV
    pixel_hsv = cv.cvtColor(np.uint8([[pixel_bgr_Array]]), cv.COLOR_BGR2HSV)[0][0]

    # Convert BGR to Grayscale
    pixel_gray = cv.cvtColor(np.uint8([[pixel_bgr_Array]]), cv.COLOR_BGR2GRAY)[0][0]

    # Convert BGR to Lab (CIELAB)
    pixel_lab = cv.cvtColor(np.uint8([[pixel_bgr_Array]]), cv.COLOR_BGR2Lab)[0][0]

    # Convert BGR to YUV
    pixel_yuv = cv.cvtColor(np.uint8([[pixel_bgr_Array]]), cv.COLOR_BGR2YUV)[0][0]

    # Convert BGR to HLS
    pixel_hls = cv.cvtColor(np.uint8([[pixel_bgr_Array]]), cv.COLOR_BGR2HLS)[0][0]

    x=x+1
    print('UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU',)
    print('Pixel ', x)
    print('Pixel color BGR:', pixel_bgr) #Print the pixel in
    print('Pixel color RGB:', pixel_rgb) #Print the pixel in
    print('Pixel color HSV:', pixel_hsv) #Print the pixel in
    print('Pixel color Grayscale:', pixel_gray) #Print the pixel in
    print('Pixel color Lab:', pixel_lab) #Print the pixel in
    print('Pixel color Yuv:', pixel_yuv) #Print the pixel in
    print('Pixel color HLS:', pixel_hls) #Print the pixel in
    









    img = cv.rectangle(video_RS, ((size//2)-size//100*2,(size//2)-size//100*2), ((size//2)+size//100*2, (size//2)+size//100*2), (0, 0, 255), 1)
    img = cv.line(img, ((size//2), (size//2)-size//100*2), ((size//2),(size//2)-1), (0, 0, 255), 1)

    cv.imshow("Video", img) #Here we create a window which shows the video/image

    if cv.waitKey(1) == ord('q'): #If q is pressed while this is running, break the while loop
        break


cap.release() #make the camera available again
cv.destroyAllWindows() # close all windows







