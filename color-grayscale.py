import cv2 as cv
import numpy as np

	
image = cv2.imread('C:/Users/N/Desktop/Test.jpg')

# Convert Color to GrayScale
grayScale = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# Convert to Black and White

(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)

cv.imshow('Original Image',image)
cv.imshow('Gray Scale',grayScale)

k = cv.waitKey(0)
cv.destroyAllWindows()
