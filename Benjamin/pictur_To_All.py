import numpy as np
import cv2 as cv


cap = cv.VideoCapture(0)

size = 200
x=0
print('program initiation')
while True:
    #ret, frame = cap.read() #ret is checking if the function works, but if it is i will save the camera output from camera "0" as frame
    #idth = int(cap.get(3)) #cap.get retrieves information from the capture, in this case the third information which is width
    #height = int(cap.get(4)) #and here the 4th, which is height
    
    frame = cv.imread('stenbilleder.jpg')

    BGR = cv.resize(frame, (size, size)) #Resize image
    image = np.zeros((size*4, size*4), dtype = 'uint8')
    blank = np.zeros(BGR.shape[:2], dtype = 'uint8') #Brug denne til at indsætte som tom i de andre farvekanaler
    b, g, r = cv.split(BGR) #Opdel BGR i dens tre kanaler
    blue = cv.merge([b,blank,blank]) 
    green = cv.merge([blank,g,blank])
    red = cv.merge([blank,blank,r])

    HSV = cv.cvtColor(BGR, cv.COLOR_BGR2HSV)
    H, S, V = cv.split(HSV)
    hue = cv.merge([H,blank,blank])
    sat = cv.merge([blank,S,blank])
    val = cv.merge([blank,blank,V])


    HLS = cv.cvtColor(BGR, cv.COLOR_BGR2HLS)
    HU, SA, LI = cv.split(HLS)
    hue = cv.merge([H,blank,blank])
    sat = cv.merge([blank,S,blank])
    val = cv.merge([blank,blank,V])


    YUV = cv.cvtColor(BGR, cv.COLOR_BGR2YUV)
    Y, U, UV = cv.split(YUV)
    hue = cv.merge([H,blank,blank])
    sat = cv.merge([blank,S,blank])
    val = cv.merge([blank,blank,V])



    #YUV = cv.cvtColor(BGR, cv.COLOR_BGR2YUV)
    #LAB = cv.cvtColor(BGR, cv.COLOR_BGR2Lab)





    #print(image.shape)
    #øverste række BGR
    #image[ :size, :size] = blue+green+red
    image[ :size, size:size*2] = b
    image[ :size, size*2:size*3] = g
    image[ :size, size*3:size*4] = r

    #anden række HSV
    #image[ size:size*2, :size] = blue+green+red
    image[ size:size*2, size:size*2] = H
    image[ size:size*2, size*2:size*3] = S
    image[ size:size*2, size*3:size*4] = V

    #Tredje række HSL
    #image[ size:size*2, :size] = blue+green+red
    image[ size*2:size*3, size:size*2] = HU
    image[ size*2:size*3, size*2:size*3] = SA
    image[ size*2:size*3, size*3:size*4] = LI


    image[ size*3:size*4, size:size*2] = Y
    image[ size*3:size*4, size*2:size*3] = U
    image[ size*3:size*4, size*3:size*4] = UV

    #print(H)
    #image[ :size, :size*4] = red

    #cv.imshow("BGR", BGR)
    #cv.imshow("blue", blue)
    cv.imshow("HSV", image)
    #cv.imshow("YUV", YUV)
    #cv.imshow("LAB", LAB)



    if cv.waitKey(1) == ord('q'): #If q is pressed while this is running, break the while loop
        break
    
cap.release() #make the camera available again
cv.destroyAllWindows() # close all windows



