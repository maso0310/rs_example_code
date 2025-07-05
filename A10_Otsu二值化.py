import cv2 as cv
import glob 
from pathlib import Path 
image = cv.imread(glob.glob('./*/*.png')[0])
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
ret, Otsu = cv.threshold(gray, 127, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
# 顯示灰階、二值化圖片
cv.imshow('灰階', gray)
cv.imshow('基礎二值化', binary)
cv.imshow('Otsu二值化', Otsu)
cv.waitKey()
