import cv2 as cv
import numpy as np

# Load the YUV image

bgr_image = cv.imread('Benjamin\stenbilleder.jpg')

yuv_image = cv.cvtColor(bgr_image, cv.COLOR_BGR2YUV)

# Split the YUV image into its Y, U, and V components
y, u, v = cv.split(yuv_image)

# Create placeholder images for Y and V components with all zeros
y_color = np.zeros_like(y)
v_color = np.zeros_like(v)

# Merge the Y, U, and V components to create a BGR color image
yuv_color_image = cv.merge((y, u, v))

# Convert the YUV color image to RGB
rgb_image = cv.cvtColor(yuv_color_image, cv.COLOR_YUV2BGR)
# Create color-mapped images for U and V components

u_color = cv.applyColorMap(u, cv.COLORMAP_JET)  # Blue-Yellow gradient
v_color = cv.applyColorMap(v, cv.COLORMAP_HOT)   # Red-Green gradient

# Display the Y, U, and V components in separate windows
cv.imshow('Y Component (Luma)', y)
cv.imshow('U Component (Chroma Blue)', u_color)
cv.imshow('V Component (Chroma Red)', v_color)

# Display the RGB image for reference
cv.imshow('RGB Image', rgb_image)

# Wait for a key press and close all windows
cv.waitKey(0)
cv.destroyAllWindows()