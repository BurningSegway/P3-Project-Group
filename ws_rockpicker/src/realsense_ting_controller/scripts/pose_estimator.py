import numpy as np
import cv2 as cv
import glob

with np.load("/home/pe/ws_rockpicker/src/realsense_ting_controller/scripts/CameraParams.npz") as file:
    mtx, dist, r_vecs, t_vecs = [file[i] for i in ('matrix', 'distortion', 'r_vecs', 't_vecs')]

criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)


#mtx = np.zeros((3, 3), np.float32)
#mtx[0, 0] = 1382.0665283203125
#mtx[0, 1] = 0
#mtx[0, 2] = 946.7578125

#mtx[1, 0] = 0
#mtx[1, 1] = 1382.5836181640625
#mtx[1, 2] = 554.0628662109375

#mtx[2, 0] = 0
#mtx[2, 1] = 0
#mtx[2, 2] = 1

print(mtx)

objp = np.zeros((2*2,3), np.float32)
objp[:,:2] = np.mgrid[0:2, 0:2].T.reshape(-1,2)

#objp = np.zeros((4, 3), np.float32)
imgp = np.zeros((4, 2), np.float32)
imgp[0] = [250, 470]
imgp[1] = [500, 780]
imgp[2] = [1500, 500]
imgp[3] = [700, 666]



print(objp)
print(imgp)

img = cv.imread('/home/pe/ws_rockpicker/src/realsense_ting_controller/scripts/Image_1.jpg')
print(img.shape[:2])
h, w = img.shape[:2]
new_mtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

undist = cv.undistort(img, mtx, dist, None, None)

ret, rot_vecs, tran_vecs = cv.solvePnP(objp, imgp, mtx, dist)

print(f"Rotation: {rot_vecs}")
print(f"Translation: {tran_vecs}")

rotmatrix = np.zeros(shape=(3,3))

cv.Rodrigues(rot_vecs, rotmatrix)
print(f"Rotation Matrix: {rotmatrix}")

point = np.array([3, 0, 0], np.float32)

print(point)

imgpts, jac = cv.projectPoints(point, rot_vecs, tran_vecs, mtx, dist)

print(imgpts)

x, y, w, h = roi
#undist = undist[y:y+h, x:x+w]

cv.circle(undist, (400, 210), 2, (255, 0, 0), 2)

cv.imshow("distorted", img)
cv.imshow("undistorted", undist)
cv.waitKey(0)