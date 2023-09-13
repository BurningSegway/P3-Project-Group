import numpy as np
import cv2 as cv

# Chosen color in BGR format (blue, green, red)
chosen_color_bgr = np.array([64, 77, 42])  # For example, red color

# Convert the chosen color to HSV
chosen_color_hsv = cv.cvtColor(np.uint8([[chosen_color_bgr]]), cv.COLOR_BGR2HSV)[0][0]

# Define a range for varying hue values (e.g., -30 to +30 degrees)
hue_range = 30

# Calculate lower and upper bounds for the hue
lower_hue = (chosen_color_hsv[0] - hue_range) % 180  # Hue values wrap around 0-179
upper_hue = (chosen_color_hsv[0] + hue_range) % 180

# Define constant values for saturation and value (you can adjust these as needed)
constant_saturation = 255
constant_value = 255

# Create lower and upper bounds for the color range in HSV
lower_bound = np.array([lower_hue, constant_saturation, constant_value], dtype=np.uint8)
upper_bound = np.array([upper_hue, constant_saturation, constant_value], dtype=np.uint8)

print("Lower HSV Bound:", lower_bound)
print("Upper HSV Bound:", upper_bound)