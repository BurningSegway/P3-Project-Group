import cv2
import numpy as np

with np.load("/home/pe/ws_rockpicker/src/realsense_ting_controller/scripts/CameraParams.npz") as file:
    mtx, dist, r_vecs, t_vecs = [file[i] for i in ('matrix', 'distortion', 'r_vecs', 't_vecs')]

mtx = np.array([[1382.0665283203125, 0, 946.7578125],[0, 1382.5836181640625, 554.0628662109375], [0, 0, 1]])

print(mtx)

fx = mtx[0,0]
print(fx)

fy = mtx[1,1]
print(fy)

cx = mtx[0,2]
print(cx)

cy = mtx[1,2]
print(cy)

# Pixel coordinates
#u = 1252
#v = 787

u = 470
v = 450

pixel_coords = np.array([[u, v]], dtype=np.float32)

identity = np.identity(3)

# Undistort pixel coordinates
undistorted_coords = cv2.undistortPoints(pixel_coords, mtx, dist)

# Normalized coords https://medium.com/@sim30217/pixel-coordinates-and-normalized-image-coordinates-126c83b91379
xn = (u-cx)/fx
yn = (v-cy)/fy

normalized_coords = np.array([[xn, yn]], dtype=np.float32)

print(f"Undistorted points: {undistorted_coords}")
print(f"Normalized points: {normalized_coords}")
