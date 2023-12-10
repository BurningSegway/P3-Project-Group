import numpy as np
import cv2 as cv
import glob

with np.load("/home/pe/ws_rockpicker/src/realsense_ting_controller/scripts/CameraParams.npz") as file:
    mtx, dist, r_vecs, t_vecs = [file[i] for i in ('matrix', 'distortion', 'r_vecs', 't_vecs')]

criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

objp = np.zeros((9*6, 3), np.float32)
objp[:,:2] = np.mgrid[0:9, 0:6].T.reshape(-1,2)

img = cv.imread("/home/pe/ws_rockpicker/src/realsense_ting_controller/scripts/Image_1.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, corners = cv.findChessboardCorners(gray, (9,6), None)

if ret == True:
    corners2 = cv.cornerSubPix(gray, corners, (11,11),(-1,-1), criteria)

    ret, rvecs, tvecs = cv.solvePnP(objp, corners2, mtx, dist)

    help = np.array([0, 1, 0], np.float32)

    imgpts, jac = cv.projectPoints(help, rvecs, tvecs, mtx, dist)

print(f"Rotation: {rvecs}")
print(f"Translation: {tvecs}")

rotmatrix = np.zeros(shape=(3,3))

cv.Rodrigues(rvecs, rotmatrix)
print(f"Rotation Matrix: {rotmatrix}")
print(f"Imgpts? {imgpts}")