import cv2
import numpy as np

# Load an image from file
image = cv2.imread('prof_voyles.jpeg', cv2.IMREAD_GRAYSCALE)

# Apply GaussianBlur to reduce noise and help Canny edge detection
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Use Canny edge detector
edges = cv2.canny(blurred,35,43)

# Display the original and edges images
cv2.imshow('Original Image', image)
cv2.imshow('Canny Edges', edges)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
