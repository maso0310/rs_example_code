import cv2 as cv

image = cv.imread('./01_Image/Lenna.png')

cv.imshow('Lenna', image)
cv.waitKey()

print(image)
print(image.shape)