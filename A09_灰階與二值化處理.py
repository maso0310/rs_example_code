import cv2 as cv
import glob 
from pathlib import Path 
image = cv.imread(glob.glob('./*/*.png')[0])
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
ret, binary1 = cv.threshold(gray, 50, 255, cv.THRESH_BINARY)
ret, binary2 = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
# 顯示灰階、二值化圖片
cv.imshow('灰階', gray)
cv.imshow('二值化1', binary1)
cv.imshow('二值化2', binary2)
cv.waitKey()