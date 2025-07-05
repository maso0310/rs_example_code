import os
import glob
from osgeo import gdal
i=0
for image_path in glob.glob('./03_Result/*.tif'):
    image = gdal.Open(image_path).ReadAsArray() / 255.0
    R = image[0,:,:]
    G = image[1,:,:]
    B = image[2,:,:]
    ExG = (2 * G) - R - B
    os.makedirs('./03_Result/VIs', exist_ok=True)
    image_writer = gdal.Translate(f'./03_Result/VIs/ExG_{i}.tif', image_path, bandList=[1], outputType=gdal.GDT_Float32)
    image_writer.WriteArray(ExG)
    i+=1

print('植生指標計算與繪圖完畢！')