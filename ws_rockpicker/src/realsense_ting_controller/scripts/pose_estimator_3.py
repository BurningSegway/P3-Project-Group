import cv2
import numpy as np

with np.load("/home/pe/ws_rockpicker/src/realsense_ting_controller/scripts/CameraParams.npz") as file:
    mtx, dist, r_vecs, t_vecs = [file[i] for i in ('matrix', 'distortion', 'r_vecs', 't_vecs')]

# Rotation and translation vectors from solvePnP
rvec = np.array([[-0.00590822], [-0.01743749], [-0.00141489]])
tvec = np.array([[-3.77806537], [-2.15464099], [26.31565521]])

# Pixel coordinates
pixel_coords = np.array([[470, 450]], dtype=np.float32)

# Undistort pixel coordinates
undistorted_coords = cv2.undistortPoints(pixel_coords, mtx, dist)

print(undistorted_coords)

# Separate rotation matrix and translation vector
rotation_matrix, _ = cv2.Rodrigues(rvec)
transformation_matrix = np.hstack((rotation_matrix, tvec))
print(transformation_matrix)

# Use the rotation and translation matrices to transform to world coordinates
world_coords = np.dot(np.linalg.inv(transformation_matrix), np.append(undistorted_coords, 1))

# Print the result
print("World Coordinates:", world_coords)
