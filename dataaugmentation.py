import cv2
import numpy as np

# Read image
coffee_cup = cv2.imread('coffee_cup.jpg')

# Convert to HSV color space
hsv_image = cv2.cvtColor(coffee_cup, cv2.COLOR_BGR2HSV)

# Adjust hue and saturation
hsv_image[:, :, 0] = np.clip(hsv_image[:, :, 0] + np.random.randint(-20, 20), 0, 179)
hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1] + np.random.randint(-30, 30), 0, 255)

# Convert back to BGR
augmented_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

# Display augmented image
cv2.imshow('Augmented Image', augmented_image)
