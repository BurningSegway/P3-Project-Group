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
    image = cv.imread("/home/pe/ws_rockpicker/src/realsense_ting_controller/scripts/Image.jpg")
    #image = cv.resize(image, (1280, 720)) #resize if you want to look at the pictures, for actual coordinates, uncomment
    

    cmd = data.request

    if cmd == "Process":
        print("Process image")

        main_thresh = 63

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
    brightened = cv.add(image, np.array([40.0]))
    HSVImage = cv.cvtColor(brightened, cv.COLOR_BGR2HSV)
    H, S, V = cv.split(HSVImage) 
    #cv.imshow("S", S) #
    print("her2")
    gaussian = cv.GaussianBlur(S, (7, 7), 0)
    #cv.imshow("Gaussian", gaussian)#
    # Thresholding the saturation channel,
    thresholded = cv.threshold(S, threshold, 255, cv.THRESH_BINARY)[1]
    thresholded = cv.bitwise_not(thresholded)
    #cv.imshow("Thresholded", thresholded)#
    #cv.waitKey(0)#
    
    dilated = cv.dilate(thresholded, (3, 3), iterations=2)
    #Finding contours and drawing the small contours on a mask, based on size
    eroded = cv.erode(thresholded, (3, 3), iterations=2)
    opening = cv.morphologyEx(eroded, cv.MORPH_OPEN, (3, 3), iterations=2)
    #cv.imshow("Opening", opening)    
    #cv.imshow("Eroded", eroded)
    #cv.waitKey(0)
    contours = cv.findContours(dilated, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]
    small_contours = [cnt for cnt in contours if cv.contourArea(cnt) < 1000]
    mask = np.zeros_like(thresholded)
    cv.drawContours(mask, small_contours, -1, (255, 255, 255), -1)
    #cv.imshow("Mask", mask)#

    #Subtracting the small contours from the thresholded image
    subtractedSmall = cv.subtract(thresholded, mask)
    dilated = cv.dilate(subtractedSmall, (3, 3), iterations=2)
    contours2 = cv.findContours(dilated, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]
    contour_img = np.zeros_like(image)
    #cv.imshow("SubtractedSmall", subtractedSmall)#
    #Drawing filled contours on the contour_img
    drawCont = cv.drawContours(contour_img, contours2, -1, (255, 255, 255), -1)
    #cv.imshow("Contours", contour_img)
    #cv.imshow("Contour",contour_img)#

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

    return contours2, contour_img


def watershed(image, x):
    contour_img = x
    water_thresh = 30
    #checking if image contains anything
    if np.sum(image) == 0:
        return []
    else:
        #Morphological opening
        kernel = np.ones((3, 3), np.uint8)
        opening = cv.morphologyEx(image, cv.MORPH_OPEN, kernel, iterations=10)
        opening = np.uint8(opening)
        opening_gray = cv.cvtColor(opening, cv.COLOR_BGR2GRAY)

        #Finding sure background and foreground through dilation and distance transform thresholding
        sure_bg = cv.dilate(opening, kernel, iterations=2)
        distance_transform = cv.distanceTransform(opening_gray, cv.DIST_L2, 5)
        normalized_distance = exposure.rescale_intensity(distance_transform, out_range=(0, 255))
        normalized_distance = normalized_distance.astype(np.uint8)
        _, distThres = cv.threshold(distance_transform, water_thresh, 255, cv.THRESH_BINARY)
        sure_bg = cv.cvtColor(sure_bg, cv.COLOR_BGR2GRAY)
        distThres = np.uint8(distThres)

        #cv.imshow("Normalized Distance", normalized_distance)
        #print("Sure_bg", sure_bg.shape)
        #print("distThres", distThres.shape)
        #cv.waitKey(0)
        #Finding unknown region
        unknown = cv.subtract(sure_bg, distThres)
        #cv.imshow("sure_bg", sure_bg)
        #cv.imshow("distThres", distThres)
        #cv.imshow("Unknown", unknown)
        #cv.waitKey(0)

        #Labeling the markers, 
        labels = cv.connectedComponents(distThres, connectivity=8, ltype=cv.CV_32S)[1]
        labels = labels + 1

        #Marking the unknown region with zero
        labels[unknown == 255] = 0

        mask = np.zeros_like(image)
        mask2 = np.zeros_like(image)
        #Watershed
        labels = cv.watershed(contour_img, labels)
        mask[labels == -1] = [255, 0, 0]
        uniqueLabels = np.unique(labels)
        print(uniqueLabels)
        LabelContours = []
        for label in uniqueLabels:
            if label == -1 or label == 1:
                continue
            labelMask = np.zeros_like(image)
            labelMask[labels == label] = 255
            labelMask = cv.cvtColor(labelMask, cv.COLOR_BGR2GRAY)
            contours = cv.findContours(labelMask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]
            LabelContours.append(contours)
    
        return LabelContours
        

def process_main(image, threshold):

    image = image

    image2 = image.copy()
    image3 = image.copy()
    img_h, img_w = image.shape[:2]

    #cv.imshow("test", image)#

    #Preproccesing
    contours2, contour_img = Preproccesing(image, threshold)

   

    #Creating lists for sorting contours, and establishing thresholds
    InBoundRock = []
    OutBoundRock = []
    SortHull = []
    SingleRock = []
    MultipleRocks = []
    SolidityThres = 0.85
    EllipseThres = 0.80
    LowerSolidityThres = 0.50
    LowerEllipseThres = 0.50

    #Sorting contours based on convex and ellipse solidity, and based on image boundaries
    for cnt in contours2:
        SortingConvexHull = cv.convexHull(cnt)
        SortingEllipse = cv.fitEllipse(SortingConvexHull)
        Area = cv.contourArea(cnt)
        ConvexHullArea = cv.contourArea(SortingConvexHull)
        EllipseArea = (SortingEllipse[1][0]/2)*(SortingEllipse[1][1]/2)*np.pi
        Solidity = float(Area)/ConvexHullArea
        SolidityEllipse = float(Area)/EllipseArea
        #print(Solidity)
        #print(SolidityEllipse)
        cv.ellipse(image2, SortingEllipse, (0, 255, 0), 2)
        if 15 < SortingEllipse[0][0] < img_w-15 and 15 < SortingEllipse[0][1] < img_h-15:
            InBoundRock.append(SortingEllipse)
            SortHull.append(SortingConvexHull)
            if Solidity < SolidityThres and SolidityEllipse < EllipseThres:
                MultipleRocks.append(cnt)
            else:
                SingleRock.append(cnt)
        else:
            OutBoundRock.append(SortingEllipse)


    MultipleRockImg = np.zeros_like(image)
    SingleRockImg = np.zeros_like(image)

    cv.drawContours(MultipleRockImg, MultipleRocks, -1, (255, 255, 255), -1)
    cv.drawContours(SingleRockImg, SingleRock, -1, (255, 255, 255), -1)

    filename = '/home/pe/ws_rockpicker/src/realsense_ting_controller/scripts/Image_Rocks.jpg' 
    cv.imwrite(filename, MultipleRockImg)
    #cv.imshow("MultipleRockImg", MultipleRockImg)#
    #cv.imshow("SingleRockImg", SingleRockImg)#


    LabelContours = watershed(MultipleRockImg, contour_img)
    AllEllipse = []
    AllContours = []
    FinalImg = np.zeros_like(image)
    print(FinalImg.shape)
    FinalImg[SingleRockImg == 255] = 255
    AllContours.extend(SingleRock)

    for contours in LabelContours:
        AllContours.extend(contours)
        cv.drawContours(FinalImg, contours, -1, (255, 255, 255), -1)
        
    for cnt in AllContours:
        ellipse = cv.fitEllipse(cnt)
        #print(ellipse)
        AllEllipse.append(ellipse)
        cv.ellipse(image3, ellipse, (0, 255, 0), 2)
        

    #Sorting ellipses based on longest axis
    for ellipse in AllEllipse:
        SortedEllipse = sorted(AllEllipse, key=lambda x: max(x[1]), reverse=True)
        cv.circle(image3, (int(ellipse[0][0]), int(ellipse[0][1])), 4, (255, 0, 0), -1)

    cv.ellipse(image3, SortedEllipse[0], (0, 0, 255), 2)
    
    
    #cv.imshow("Image2", image2)#
    #cv.imshow("Image3", image3)#
    #cv.imshow("FinalImg", FinalImg)#
    image_small = cv.resize(image3, (1280, 720))#
    #cv.imshow("Small", image_small)#
    #cv.resizeWindow("FinalImg", 600, 600)#
    #cv.waitKey(0)#
    #cv.destroyAllWindows()#
    global number
    global stamp
    
    filename = '/home/pe/ws_rockpicker/src/realsense_ting_controller/scripts/Image_ellipse.jpg'
    cv.imwrite(filename, image_small)
    filename = '/home/pe/ws_rockpicker/src/realsense_ting_controller/scripts/final_test/Image_ellipse_'+str(stamp)+'_'+str(number)+'.jpg'
    cv.imwrite(filename, image3)

    number += 1
    
    return SortedEllipse

def GetList(a, x, y):
    SortedEllipse = a

    if x == 1 and y == 0:
        return SortedEllipse[0]
    if y == 1:
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