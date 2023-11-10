########################################################################################################################
#cropImgs.py
#
#
########################################################################################################################
import os
import cv2
import numpy as np
from optparse import OptionParser


parser = OptionParser()

parser.add_option("-c", "--class", dest="class_type", help="image class", default="cat")
parser.add_option("-t", "--type", dest="run4", help="run for train or test", default="train")
parser.add_option("-i", "--input", dest="input_path", help="Path to input segmented images.", default="../MetaData/CatsDog/Imgs/")
parser.add_option("-o", "--output", dest="output_path", help="Path to res file.", default="../MetaData/CatsDog/SegImgs/")
parser.add_option("-n", "--nos", dest="seg_nos", help="no of segments", default="8")

(options, args) = parser.parse_args()

for run4 in ['train', 'test']:
    for class_type in ['cat', 'dog']:
        imgs_path = options.input_path + run4 + "/" + class_type
        imgs_seg_path = options.output_path + run4 + "/" + class_type
        
        for idxClass, imgName in enumerate(sorted(os.listdir(imgs_path))):
            if not imgName.lower().endswith(('.bmp', '.jpeg', '.jpg', '.png', '.tif', '.tiff')):
                continue
    
            filepath = os.path.join(imgs_path, imgName)
            ##############################################################
            #load img
            img = cv2.imread(filepath)            
            (rows, cols) = img.shape[:2]
            n_width = int(cols)
            n_height = int(rows)
            seg_name, seg_ext = os.path.splitext(imgName)
            
            n_div = 3
            n_vrsn = 1
            f_overlap = 0.1
            f_fctr_min = (1-f_overlap)/n_div
            f_fctr_max = (1+f_overlap)/n_div
                        
            for y in range(n_div):
                for x in range(n_div):
                    x_min = int(n_width * x * f_fctr_min)
                    y_min = int(n_height * y * f_fctr_min)
                    
                    x_max = int(n_width * (x+1) * f_fctr_max)
                    y_max = int(n_height * (y+1) * f_fctr_max)
                    
                    if x_min < 0:
                        x_min = 0
                    if y_min < 0:
                        y_min = 0
                    
                    if x_max > n_width:
                        x_max = n_width
                    if y_max > n_height:
                        y_max = n_height
                    
                    #print(str(x_min) + ", " + str(y_min) + ", " + str(x_max) + ", " + str(y_max))
                    #crop the img
                    seg_img = img[y_min:y_max, x_min:x_max]
                    seg_imgname = seg_name + "_" + str(n_vrsn) + seg_ext
                
                    seg_filepath = os.path.join(imgs_seg_path, seg_imgname)
                
                    cv2.imwrite(seg_filepath, seg_img)
                    n_vrsn+=1
'''            
            y_min = 0
            x_min = 0
            x_max = n_width/2
            x_max = n_width//2
            y_max = n_height//2
            
            
            
            
            nLen = len(seg_ext)
            str_vrsn = "_1"
            
            seg_imgname = seg_name + str_vrsn + seg_ext
        
            seg_filepath = os.path.join(imgs_seg_path, seg_imgname)
        
            cv2.imwrite(seg_filepath, seg_img)
            
'''            
            
            
            
            