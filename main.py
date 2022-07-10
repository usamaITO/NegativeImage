import cv2

# open image using cv
image = cv2.imread('image.jpeg')
# formula for negative image
L = 256   # Number of Levels
negativeImage = (L-1)-image  # negative image
# showing negative image
cv2.imshow('Original Image', image)
cv2.imshow('Negative image', negativeImage)

cv2.waitKey(0)
cv2.destroyAllWindows()