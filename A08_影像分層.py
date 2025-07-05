import cv2 as cv
import glob
from pathlib import Path
image_path = glob.glob('./01_Image/Lenna.png')[0]
image_name = Path(image_path).stem
image = cv.imread(image_path)
# 將B、G、R圖層分離出來
B = image[:,:,0]
G = image[:,:,1]
R = image[:,:,2]
cv.imshow('B', B)
cv.imshow('G', G)
cv.imshow('R', R)
cv.waitKey()