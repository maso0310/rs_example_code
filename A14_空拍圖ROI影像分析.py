import glob 
from pathlib import Path
from osgeo import gdal
import os
from skimage.filters import threshold_otsu

image_path_list = glob.glob('./03_Result/*.tif')

for i in range(len(image_path_list)):
    image_path = image_path_list[i]
    image = gdal.Open(image_path).ReadAsArray() / 255.0
    image_name = Path(image_path).stem

    R = image[0,:,:]
    G = image[1,:,:]
    B = image[2,:,:]

    ExG = 2*G - R - B
    thread_val = threshold_otsu(ExG)
    mask = (ExG > thread_val) * 1.0
    print(f'Otsu閾值為： {thread_val}')

    new_image = image * mask * 255.0
    os.makedirs(f'./03_Result/Otsu', exist_ok=True)
    image_writer = gdal.Translate(f'./03_Result/Otsu_Result_{i}.tif',   image_path, outputType=gdal.GDT_Byte)
    image_writer.WriteArray(new_image)
