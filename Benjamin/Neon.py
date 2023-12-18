import cv2 as cv
import numpy as np


#Use Python and OpenCV to load and display neon-text.png 

#Use template matching to make an image which shows the positions of the three hearts, similar to the one below 
#(the white dots showing the positions are very small, but there are three of them). Show the correlation image as an intermediate step. 
#Hint: Use a combination of the functions matchTemplate, normalize, and threshold 
#
#



Image = cv.imread('Benjamin\\neon-text.png', 0)
template = cv.imread('Benjamin\Template.png', 0)
New_Image = cv.imread('Benjamin\\neon-text.png')
w,h = template.shape

res = cv.matchTemplate(Image,template,cv.TM_CCOEFF_NORMED)
threshold = 0.8
print(res.shape)
location = np.where( res >= threshold)
for pt in zip(*location[::-1]):
    New_Image = cv.circle(New_Image, (pt[0] + w//2, pt[1] + h//5), 1, (255, 255, 255), -1)



cv.imshow("Farver", Image)
cv.imshow("Template", template)
cv.imshow("New_Image", New_Image)
cv.waitKey()

    

#cap.release() #make the camera available again
cv.destroyAllWindows() # close all windows





