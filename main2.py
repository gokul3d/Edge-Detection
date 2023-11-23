import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image from file
image = cv2.imread('door.jpeg', cv2.IMREAD_GRAYSCALE)

# Apply Sobel operator for edge detection
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Compute the gradient magnitude
gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

# Display the original image and the Sobel edges
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1), plt.imshow(image, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(1, 3, 2), plt.imshow(np.abs(sobel_y), cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.subplot(1, 3, 3), plt.imshow(gradient_magnitude, cmap='gray')
plt.title('Gradient Magnitude'), plt.xticks([]), plt.yticks([])

plt.show()
