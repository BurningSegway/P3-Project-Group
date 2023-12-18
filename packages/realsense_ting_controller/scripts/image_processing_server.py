#!/usr/bin/env python3

import rospy
import cv2 as cv
import numpy as np
import skimage.exposure as exposure
from realsense_ting_controller.srv import *

from realsense_ting_controller.srv import ImgProc, ImgProcResponse

import datetime

date_time = datetime.datetime.now()

stamp = str(date_time.year)+'_'+str(date_time.month)+'_'+str(date_time.day)+'_'+str(date_time.hour)+'_'+str(date_time.minute)

number = 1

def process_image(data):
    print(image_command_client("Capture"))

    rospy.sleep(0.5)

    #Load image and get image dimensions
    image = cv.imread("/home/pe/ws_rockpicker/src/realsense_ting_controller/scripts/Image.jpg") #Load the image with OpenCV
    #image = cv.resize(image, (1280, 720)) #resize if you want to look at the pictures, for actual coordinates, uncomment
    

    cmd = data.request

    if cmd == "Process":
        print("Process image")

        main_thresh = 63 #Threshold for saturation channel, passed as the second variable in the Preproccesing function

        SortedEllipse = process_main(image, main_thresh)
        print(SortedEllipse)
        print(GetList(SortedEllipse, 1, 0))

        #print(GetList(2,1))

        list = GetList(SortedEllipse, 1,0)
        array1 = list[0]
        array2 = list[1]
        array3 = list[2]
        arrayproper = []
        print(array1)
        print(array2)
        print(array3)
        arrayproper.append(array1[0])
        arrayproper.append(array1[1])
        arrayproper.append(array2[0])
        arrayproper.append(array2[1])
        arrayproper.append(array3)

        print(arrayproper)

        #cv.destroyAllWindows()#

        return ImgProcResponse(arrayproper)

def main():

    rospy.init_node('image_processor_server', anonymous=True)

    s = rospy.Service('process_image', ImgProc, process_image)
    print("Ready to recieve command")



    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv.destroyAllWindows()


def Preproccesing(image, threshold):
    # Convert to HSV and split into channels
    brightened = cv.add(image, np.array([40.0])) #Brightening the image for better results
    HSVImage = cv.cvtColor(brightened, cv.COLOR_BGR2HSV) #Converting to HSV with OpenCV
    H, S, V = cv.split(HSVImage) #Splitting the image into channels, H = Hue, S = Saturation, V = Value
    #cv.imshow("S", S) #Debugging
    print("her2")
    gaussian = cv.GaussianBlur(S, (7, 7), 0) #DEN HER MÅ GERNE SLETTES, BRUGES IKKE 
    #cv.imshow("Gaussian", gaussian) #DEN HER MÅ GERNE SLETTES, BRUGES IKKE

    # Thresholding the saturation channel, 
    thresholded = cv.threshold(S, threshold, 255, cv.THRESH_BINARY)[1] #Thresholding the saturation channel with a variable threshold
    thresholded = cv.bitwise_not(thresholded) #Inverting the thresholded image as the rocks are dark and the background is light
    #cv.imshow("Thresholded", thresholded) #Debugging
    #cv.waitKey(0) #Debugging
    
    #Dilating and finding contours in the image
    dilated = cv.dilate(thresholded, (3, 3), iterations=2) #Dilating the thresholded image to make the contours more clear and allowing for sorting
    eroded = cv.erode(thresholded, (3, 3), iterations=2) #DEN HER MÅ GERNE SLETTES, BRUGES IKKE
    opening = cv.morphologyEx(eroded, cv.MORPH_OPEN, (3, 3), iterations=2) #DEN HER MÅ GERNE SLETTES, BRUGES IKKE
    #cv.imshow("Opening", opening) #DEN HER MÅ GERNE SLETTES, BRUGES IKKE
    #cv.imshow("Eroded", eroded) #DEN HER MÅ GERNE SLETTES, BRUGES IKKE
    contours = cv.findContours(dilated, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0] #Finding contours in the dilated image with OpenCV
    contours = [cnt for cnt in contours if cv.contourArea(cnt) > 1000] #Sorting the contours based on size and removing the small contours <- alternativ
    contour_img = np.zeros_like(thresholded) #Creating a mask with the same dimensions as the thresholded image
    cv.drawContours(contour_img, contours, -1, (255, 255, 255), -1) #Drawing the contours on the mask

    global number
    global stamp

    filename = '/home/pe/ws_rockpicker/src/realsense_ting_controller/scripts/final_test/Image_contour_'+str(stamp)+'_'+str(number)+'.jpg'
    cv.imwrite(filename, contour_img)
    #cv.waitKey(0)#

    filename = '/home/pe/ws_rockpicker/src/realsense_ting_controller/scripts/Imagecont.jpg'
    cv.imwrite(filename, contour_img)

    filename = '/home/pe/ws_rockpicker/src/realsense_ting_controller/scripts/Image_thresh.jpg'
    cv.imwrite(filename, thresholded)

    filename = '/home/pe/ws_rockpicker/src/realsense_ting_controller/scripts/final_test/Image_threshholded_'+str(stamp)+'_'+str(number)+'.jpg'
    cv.imwrite(filename, thresholded)

    return contours, contour_img #Returning the contours and the mask with the contours drawn on it


def watershed(image, x): #Watershed labels unknown regions with known labels
    contour_img = x #hmm, ved ikke lige hvad jeg skal sige til den her.. watershed virkede bare til at være bedre med det her billede
    water_thresh = 30 #Threshold for the distance transform in current function.

    #checking if image contains anything
    if np.sum(image) == 0:
        return [] #If the image is empty, return an empty list
    else:
        #Morphological opening
        kernel = np.ones((3, 3), np.uint8) #Establishing a kernel for morphological operations
        opening = cv.morphologyEx(image, cv.MORPH_OPEN, kernel, iterations=10) #opening the image = erosion followed by dilation
        opening = np.uint8(opening) #Converting the image to uint8
        opening_gray = cv.cvtColor(opening, cv.COLOR_BGR2GRAY) #Converting the image to grayscale for distance transform, requires single channel

        #Finding sure background and foreground through dilation and distance transform thresholding
        sure_bg = cv.dilate(opening, kernel, iterations=2) #Dilating the opening to find sure background
        distance_transform = cv.distanceTransform(opening_gray, cv.DIST_L2, 5) #Finding the distance transform of the opening, distance from pixel to nearest zero pixel
        normalized_distance = exposure.rescale_intensity(distance_transform, out_range=(0, 255)) #Normalizing the distance transform to 0-255
        normalized_distance = normalized_distance.astype(np.uint8) #Converting the normalized distance transform to uint8 for vizualiation purposes
        _, distThres = cv.threshold(distance_transform, water_thresh, 255, cv.THRESH_BINARY) #Thresholding the distance transform to find sure foreground
        sure_bg = cv.cvtColor(sure_bg, cv.COLOR_BGR2GRAY) #Converting the sure background to grayscale for subtraction
        distThres = np.uint8(distThres) #Converting the distance threshold to uint8 for subtraction
        #cv.imshow("Normalized Distance", normalized_distance) #Debugging
        #print("Sure_bg", sure_bg.shape) #Debugging
        #print("distThres", distThres.shape) #Debugging
        #cv.waitKey(0) #Debugging

        #Finding unknown region 
        unknown = cv.subtract(sure_bg, distThres) #Subtracting the sure background from the distance threshold to find the unknown region
        #cv.imshow("sure_bg", sure_bg) #Debugging
        #cv.imshow("distThres", distThres) #Debugging
        #cv.imshow("Unknown", unknown) #Debugging
        #cv.waitKey(0) #Debugging

        #Labeling the markers, 
        labels = cv.connectedComponents(distThres, connectivity=8, ltype=cv.CV_32S)[1] #Labeling each component in the image for applying watershed algorithm 
        labels = labels + 1 #Adding one to the labels to avoid labeling the background as 0, since 0 is treated as unknown in watershed

        #Marking the unknown region with zero
        labels[unknown == 255] = 0 #Setting the unknown region to 0, so watershed knows to treat it as unknown

        mask = np.zeros_like(image) #Creating a mask with the same dimensions as the image
        mask2 = np.zeros_like(image) #DEN HER MÅ GERNE SLETTES, BRUGES IKKE

        #Applying Watershed
        labels = cv.watershed(contour_img, labels) #Applying watershed to the image with the markers, each region is now labeled with a unique number
        mask[labels == -1] = [255, 0, 0] #Setting the watershedded regions to blue for vizualization purposes
        uniqueLabels = np.unique(labels) #Finding the unique labels in the image
        print(uniqueLabels) #Debugging
        LabelContours = [] #Creating a list for storing the contours of the found regions
        for label in uniqueLabels: #Looping through the unique labels, so each region
            if label == -1 or label == 1: #If the label is -1 or 1, skip it, as that is background and borders
                continue
            labelMask = np.zeros_like(image) #Creating a mask with the same dimensions as the image
            labelMask[labels == label] = 255 #Where the labels are equal to the current label, set the mask to white
            labelMask = cv.cvtColor(labelMask, cv.COLOR_BGR2GRAY) #Converting the mask to grayscale for finding contours
            contours = cv.findContours(labelMask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0] #Finding contours in the mask
            LabelContours.append(contours) #Appending the contours to the list of contours
    
        return LabelContours #Returning the list of contours
        

def process_main(image, threshold):

    image = image #Load the image

    image2 = image.copy() #Creating a copy of the image for vizualization purposes and debugging
    image3 = image.copy() #Creating a copy of the image for vizualization purposes and debugging
    img_h, img_w = image.shape[:2] #Getting the height and width of the image for later use

    #cv.imshow("test", image)#

    #Preproccesing
    contours2, contour_img = Preproccesing(image, threshold) #calling the preprocessing function

    #Creating lists for sorting contours, and establishing thresholds
    InBoundRock = [] #List for storing the contours that are inside the image boundaries
    OutBoundRock = [] #List for storing the contours that are outside the image boundaries
    SortHull = [] #List for storing the convex hulls of the contours
    SingleRock = [] #List for storing the contours that are single rocks
    MultipleRocks = [] #List for storing the contours that are multiple rocks
    SolidityThres = 0.85 #Threshold for solidity of convex hull
    EllipseThres = 0.80 #Threshold for solidity of ellipse
    LowerSolidityThres = 0.50 #DEN HER MÅ GERNE SLETTES, BRUGES IKKE
    LowerEllipseThres = 0.50 #DEN HER MÅ GERNE SLETTES, BRUGES IKKE

    #Sorting contours based on convex and ellipse solidity, and based on image boundaries
    for cnt in contours2: #Looping through the contours
        SortingConvexHull = cv.convexHull(cnt) #Finding the convex hull of the contour, like a rubber band around the contour
        SortingEllipse = cv.fitEllipse(SortingConvexHull) #Fitting an ellipse to the convex hull
        Area = cv.contourArea(cnt) #Finding the area of the contour
        ConvexHullArea = cv.contourArea(SortingConvexHull) #Finding the area of the convex hull
        EllipseArea = (SortingEllipse[1][0]/2)*(SortingEllipse[1][1]/2)*np.pi #Finding the area of the ellipse
        Solidity = float(Area)/ConvexHullArea #¤Finding the solidity of contour within the convex hull
        SolidityEllipse = float(Area)/EllipseArea #Finding the solidity of the contour within the ellipse
        #print(Solidity) #Debugging
        #print(SolidityEllipse) #Debugging
        cv.ellipse(image2, SortingEllipse, (0, 255, 0), 2) #Drawing the ellipse on the image for vizualization purposes
        if 15 < SortingEllipse[0][0] < img_w-15 and 15 < SortingEllipse[0][1] < img_h-15: #Sorting the contours based on their position in the image, setting a 15 pixel boundary
            InBoundRock.append(SortingEllipse) #Appending the ellipse to the list of inbound ellipses
            SortHull.append(SortingConvexHull) #Appending the convex hull to the list of inbound convex hulls
            if Solidity < SolidityThres and SolidityEllipse < EllipseThres: #If the solidity of the convex hull and ellipse is below the threshold, the contour is from multiple rocks
                MultipleRocks.append(cnt) #Appending the contour to the list of multiple rocks
            else: #If the solidity of the convex hull and ellipse is above the threshold, the contour is from a single rock
                SingleRock.append(cnt) #Appending the contour to the list of single rocks
        else:
            OutBoundRock.append(SortingEllipse) #If the ellipse center is outside the image boundaries, append it to the list of out of bound ellipses


    MultipleRockImg = np.zeros_like(image) #Creating a mask with the same dimensions as the image
    SingleRockImg = np.zeros_like(image) #Creating a mask with the same dimensions as the image

    cv.drawContours(MultipleRockImg, MultipleRocks, -1, (255, 255, 255), -1) #Drawing the contours of the multiple rocks on the mask
    cv.drawContours(SingleRockImg, SingleRock, -1, (255, 255, 255), -1) #Drawing the contours of the single rocks on the mask

    filename = '/home/pe/ws_rockpicker/src/realsense_ting_controller/scripts/Image_Rocks.jpg' 
    cv.imwrite(filename, MultipleRockImg)
    #cv.imshow("MultipleRockImg", MultipleRockImg)#
    #cv.imshow("SingleRockImg", SingleRockImg)#


    LabelContours = watershed(MultipleRockImg, contour_img) #Calling the watershed function to segment the multiple rocks
    AllEllipse = [] #Creating a list for storing the ellipses
    AllContours = [] #Creating a list for storing the contours
    FinalImg = np.zeros_like(image) #Creating a mask with the same dimensions as the image
    print(FinalImg.shape) #Debugging
    FinalImg[SingleRockImg == 255] = 255 #Setting the single rock contours to white on the mask
    AllContours.extend(SingleRock) #Extending the list of contours with the single rock contours

    for contours in LabelContours: #Looping through the contours from the watershed function
        AllContours.extend(contours) #Extending the list of contours with the contours from the watershed function
        cv.drawContours(FinalImg, contours, -1, (255, 255, 255), -1) #Drawing the contours on the mask
        
    for cnt in AllContours: #Looping through the contours
        ellipse = cv.fitEllipse(cnt) #Fitting an ellipse to the contour
        #print(ellipse)
        AllEllipse.append(ellipse) #Appending the ellipse to the list of ellipses
        cv.ellipse(image3, ellipse, (0, 255, 0), 2) #Drawing the ellipse on the image for vizualization purposes
        

    #Sorting ellipses based on longest axis
    for ellipse in AllEllipse: #Looping through the ellipses
        SortedEllipse = sorted(AllEllipse, key=lambda x: max(x[1]), reverse=True) #Sorting the ellipses based on the longest axis, from largest to smallest
        cv.circle(image3, (int(ellipse[0][0]), int(ellipse[0][1])), 4, (255, 0, 0), -1) #Drawing a circle on the ellipse center for vizualization purposes

    cv.ellipse(image3, SortedEllipse[0], (0, 0, 255), 2) #Drawing the largest ellipse on the image with a different color for vizualization purposes
    
    
    #cv.imshow("Image2", image2) #Debugging
    #cv.imshow("Image3", image3) #Debugging
    #cv.imshow("FinalImg", FinalImg) #Debugging
    image_small = cv.resize(image3, (1280, 720)) #Resizing the image for vizualization purposes
    #cv.imshow("Small", image_small) #Debugging
    #cv.resizeWindow("FinalImg", 600, 600) #DEN HER MÅ GERNE SLETTES, BRUGES IKKE
    #cv.waitKey(0) #Debugging
    #cv.destroyAllWindows() #Debugging
    global number
    global stamp
    
    filename = '/home/pe/ws_rockpicker/src/realsense_ting_controller/scripts/Image_ellipse.jpg'
    cv.imwrite(filename, image_small)
    filename = '/home/pe/ws_rockpicker/src/realsense_ting_controller/scripts/final_test/Image_ellipse_'+str(stamp)+'_'+str(number)+'.jpg'
    cv.imwrite(filename, image3)

    number += 1
    
    return SortedEllipse #Returning the sorted ellipses

def GetList(a, x, y): #Function for getting the ellipses from the sorted list
    SortedEllipse = a #Loading the sorted ellipses

    if x == 1 and y == 0: #If the x and y values are 1 and 0, return the largest ellipse
        return SortedEllipse[0]
    if y == 1: #If the y value is 1, return the ellipse at the x value
        return SortedEllipse[x]
    
def image_command_client(c):

    rospy.wait_for_service('capture_command')

    try:
        gripper_commands = rospy.ServiceProxy('capture_command', ImageCapture)
        resp = gripper_commands(c)
        return resp.response

    except rospy.ServiceException:
        print("Service call failed :(")
 
if __name__ == '__main__':
    main()