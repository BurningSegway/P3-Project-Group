import cv2

img = cv2.imread("src/realsense_ting_controller/scripts/Image_depth_1.png", cv2.IMREAD_ANYDEPTH)

cv2.imshow("wow", img)
cv2.waitKey(0)