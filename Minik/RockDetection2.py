import cv2 as cv
import numpy as np
import skimage.exposure as exposure

#Load image and get image dimensions
image = cv.imread("Groenlaenderens_Kode/RockDetection/Billeder/Image5.jpg")
image2 = image.copy()
image3 = image.copy()
img_h, img_w = image.shape[:2]

def Preproccesing(image):
    # Convert to HSV and split into channels
    HSVImage = cv.cvtColor(image2, cv.COLOR_BGR2HSV)
    H, S, V = cv.split(HSVImage) 

    # Thresholding the saturation channel,
    thresholded = cv.threshold(S, 31.9, 255, cv.THRESH_BINARY)[1]
    cv.imshow("Thresholded", thresholded)

    #Finding contours and drawing the small contours on a mask, based on size
    contours = cv.findContours(thresholded, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]
    small_contours = [cnt for cnt in contours if cv.contourArea(cnt) < 1000]
    mask = np.zeros_like(thresholded)
    cv.drawContours(mask, small_contours, -1, (255, 255, 255), -1)
    #cv.imshow("Mask", mask)

    #Subtracting the small contours from the thresholded image
    subtractedSmall = cv.subtract(thresholded, mask)
    dilated = cv.dilate(subtractedSmall, (3, 3), iterations=2)
    contours2 = cv.findContours(dilated, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]
    contour_img = np.zeros_like(image)

    #Drawing filled contours on the contour_img
    drawCont = cv.drawContours(contour_img, contours2, -1, (255, 255, 255), -1)
    #cv.imshow("Contours", contour_img)
    return contours2, contour_img


def watershed(image):
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
        _, distThres = cv.threshold(distance_transform, 17, 255, cv.THRESH_BINARY)
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
        

def main(image):
    #Preproccesing
    contours2, contour_img = Preproccesing(image)

    #Creating lists for sorting contours, and establishing thresholds
    InBoundRock = []
    OutBoundRock = []
    SortHull = []
    SingleRock = []
    MultipleRocks = []
    SolidityThres = 0.88
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
        print(Solidity)
        print(SolidityEllipse)
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

    cv.imshow("MultipleRockImg", MultipleRockImg)
    cv.imshow("SingleRockImg", SingleRockImg)


    LabelContours = watershed(MultipleRockImg)
    AllEllipse = []
    AllContours = []
    FinalImg = np.zeros_like(image)
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

    
    cv.imshow("Image2", image2)
    cv.imshow("Image3", image3)
    cv.imshow("FinalImg", FinalImg)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return SortedEllipse

def GetList(x,y):
    if x == 0 and y == 0:
        return SortedEllipse
    if x == 1 and y == 0:
        return SortedEllipse[0]
    if y == 1:
        return SortedEllipse[x]


SortedEllipse = main(image)
print(GetList(2,1))