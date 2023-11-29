import numpy as np
import cv2 as cv


cap = cv.VideoCapture(0)

size = 285
x=0
print('program initiation')
while True:
    frame = cv.imread('Benjamin\stenbilleder.jpg')

    BGR = cv.resize(frame, (size, size)) #Resize image
    image = np.zeros((size*3, size*6), dtype = 'uint8')
    blank = np.zeros(BGR.shape[:2], dtype = 'uint8') #Brug denne til at indsætte som tom i de andre farvekanaler
    b, g, r = cv.split(BGR) #Opdel BGR i dens tre kanaler
    blue = cv.merge([b,blank,blank]) 
    green = cv.merge([blank,g,blank])
    red = cv.merge([blank,blank,r])

    HSV = cv.cvtColor(BGR, cv.COLOR_BGR2HSV)
    H, S, V = cv.split(HSV)

    HLS = cv.cvtColor(BGR, cv.COLOR_BGR2HLS)
    HU, SA, LI = cv.split(HLS)

    YUV = cv.cvtColor(BGR, cv.COLOR_BGR2YUV)
    Y, U, UV = cv.split(YUV)

    LAB = cv.cvtColor(BGR, cv.COLOR_BGR2Lab)
    LA, A, B = cv.split(YUV)




    #YUV = cv.cvtColor(BGR, cv.COLOR_BGR2YUV)
    #LAB = cv.cvtColor(BGR, cv.COLOR_BGR2Lab)





    #print(image.shape)
    #øverste række BGR
    #image[ :size, :size] = blue+green+red
    image[ :size, :size] = b
    image[ :size, size:size*2] = g
    image[ :size, size*2:size*3] = r

    #øverste række BGR
    #image[ :size, :size] = blue+green+red
    image[ :size, size*3:size*4] = LA
    image[ :size, size*4:size*5] = A
    image[ :size, size*5:size*6] = B

    #anden række HSV
    #image[ size:size*2, :size] = blue+green+red
    image[ size:size*2, :size] = H
    image[ size:size*2, size:size*2] = S
    image[ size:size*2, size*2:size*3] = V

    #Tredje række HSL
    #image[ size:size*2, :size] = blue+green+red
    image[ size:size*2, size*3:size*4] = HU
    image[ size:size*2, size*4:size*5] = SA
    image[ size:size*2, size*5:size*6] = LI


    image[ size*2:size*3, :size] = Y
    image[ size*2:size*3, size:size*2] = U
    image[ size*2:size*3, size*2:size*3] = UV

    height = 30
    font = cv.FONT_HERSHEY_SIMPLEX #Just saving a random font type as a variable
    #Text (Canvas, TEXT, placement, Font, Font size, Color, thickness, weird shit that makes "Text look better")
    image = cv.putText(image, 'Blue', (10, height), font, 1, (0, 0, 0), 2, cv.LINE_AA)
    image = cv.putText(image, 'Green', (size+10, height), font, 1, (0, 0, 0), 2, cv.LINE_AA)
    image = cv.putText(image, 'Red', (2*size+10, height), font, 1, (0, 0, 0), 2, cv.LINE_AA)
    image = cv.putText(image, 'Light', (3*size+10, height), font, 1, (0, 0, 0), 2, cv.LINE_AA)
    image = cv.putText(image, 'Red/Green', (4*size+10, height), font, 1, (0, 0, 0), 2, cv.LINE_AA)
    image = cv.putText(image, 'Blue/Yellow', (5*size+10, height), font, 1, (0, 0, 0), 2, cv.LINE_AA)

    image = cv.putText(image, 'Hue', (10, size+height), font, 1, (0, 0, 0), 2, cv.LINE_AA)
    image = cv.putText(image, 'Sat', (size+10, size+height), font, 1, (0, 0, 0), 2, cv.LINE_AA)
    image = cv.putText(image, 'Value', (2*size+10, size+height), font, 1, (0, 0, 0), 2, cv.LINE_AA)
    image = cv.putText(image, 'Hue', (3*size+10, size+height), font, 1, (0, 0, 0), 2, cv.LINE_AA)
    image = cv.putText(image, 'Sat', (4*size+10, size+height), font, 1, (0, 0, 0), 2, cv.LINE_AA)
    image = cv.putText(image, 'Light', (5*size+10, size+height), font, 1, (0, 0, 0), 2, cv.LINE_AA)

    image = cv.putText(image, 'Luma', (10, 2*size+height), font, 1, (0, 0, 0), 2, cv.LINE_AA)
    image = cv.putText(image, 'Blue', (size+10, 2*size+height), font, 1, (0, 0, 0), 2, cv.LINE_AA)
    image = cv.putText(image, 'Red', (2*size+10, 2*size+height), font, 1, (0, 0, 0), 2, cv.LINE_AA)



    cv.imshow("Gray", image)

    colormap_BG = cv.COLORMAP_JET


    image_Farver = np.zeros((size*3, size*6, 3), dtype = 'uint8')

    image_Farver[ :size, :size] = blue
    image_Farver[ :size, size:size*2] = green
    image_Farver[ :size, size*2:size*3] = red

    #YUV
    colormap_BG = cv.COLORMAP_JET
    color_image = cv.applyColorMap(U, colormap_BG)


    cv.imshow("Farver", U)



    if cv.waitKey(1) == ord('q'): #If q is pressed while this is running, break the while loop
        break
    
#cap.release() #make the camera available again
cv.destroyAllWindows() # close all windows
