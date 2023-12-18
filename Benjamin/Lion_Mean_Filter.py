import cv2 as cv
import numpy as np

BGR_Image = cv.imread('Benjamin\lion.jpg')
x,y = (10,10)
mean_Filter = np.ones((x,y), np.float32)/25
L,B,D = BGR_Image.shape
b,g,r = cv.split(BGR_Image)

def Process_Image(Image, Mean):
    processed_image = np.zeros((L-1, B-1), dtype='uint8')
    for i in range(len(processed_image)):
        for j in range(len(processed_image[i])):
            temp = Image[i-1, j-1]*Mean[0, 0]+Image[i-1, j]*Mean[0, 1]+Image[i-1, j + 1]*Mean[0, 2]+Image[i, j-1]*Mean[1, 0]+ Image[i, j]*Mean[1, 1]+Image[i, j + 1]*Mean[1, 2]+Image[i + 1, j-1]*Mean[2, 0]+Image[i + 1, j]*Mean[2, 1]+Image[i + 1, j + 1]*Mean[2, 2]
            processed_image[i, j] = temp

    return processed_image  
                
            



while True:
    #cv.imshow('LionShit', Process_Image(BGR_Image, mean_Filter))


    #BGR = cv.resize(frame, (size, size)) #Resize image
    farve = cv.merge([Process_Image(b, mean_Filter), Process_Image(g, mean_Filter), Process_Image(r, mean_Filter)])

    cv.imshow('andet billede', farve)
    cv.imshow("Farver", BGR_Image)



    if cv.waitKey(1) == ord('q'): #If q is pressed while this is running, break the while loop
        break
    
#cap.release() #make the camera available again
cv.destroyAllWindows() # close all windows
























