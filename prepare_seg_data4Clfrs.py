import os
import shutil
import re
import numpy as np
import csv
from optparse import OptionParser

parser = OptionParser()

parser.add_option("-f", "--feature_path", dest="feature_path", help="Path to features file", default="../MetaData/SegFeatures")

(options, args) = parser.parse_args()


for run4 in ['train', 'test']:
    
    #SFTI features
    for psize_sbins in ['p32b4', 'p32b3', 'p32b2', 'p64b4', 'p64b3', 'p64b2', 'p128b4', 'p128b3', 'p128b2']:
        ftrspath_clfrs = options.feature_path + "4Clfrs/" + run4 + "/sift_" + psize_sbins + ".csv"
        ftrspath_cat = options.feature_path + "/" + run4 + "/cat/siftcat_" + psize_sbins + ".csv"
        ftrspath_dog = options.feature_path + "/" + run4 + "/dog/siftdog_" + psize_sbins + ".csv"
        
        ftrs_clfrs = open(ftrspath_clfrs, 'w')
        ftrs_cat = open(ftrspath_cat,'r')
        ftrs_dog = open(ftrspath_dog,'r')
        
        curr_seg = 1
        total_segs = 9
        list_temp = []
        b_writeheader = True
        for line in ftrs_cat:
            line_split = line.strip().split(',')
            n_tokens = len(line_split)
            if b_writeheader:
                ftrs_clfrs.write('CatsDog Features\n\n')
                str_temp = 'Total Features ' + str((n_tokens-1)*total_segs) + '\t' + 'class {0,1}' + '\t' +  'Image Path\n'
                ftrs_clfrs.write(str_temp)
                b_writeheader = False
                

            list_temp.extend(line_split[:n_tokens-1])
            #n_len = len(list_temp)
            if curr_seg == total_segs:
                #append the class
                list_temp.append(0)
                img_name = line_split[n_tokens-1]
                seg_name, seg_ext = os.path.splitext(img_name)
                n_len = len(seg_name)
                img_name = seg_name[:n_len-2] + seg_ext
                list_temp.append(img_name)
                ftrs_clfrstemp = csv.writer(ftrs_clfrs)
                ftrs_clfrstemp.writerow(list_temp)
                list_temp.clear()
                curr_seg = 0
            curr_seg +=1
                    
        for line in ftrs_dog:
            line_split = line.strip().split(',')
            n_tokens = len(line_split)
            list_temp.extend(line_split[:n_tokens-1])
            if curr_seg == total_segs:
                #append the class
                list_temp.append(1)
                img_name = line_split[n_tokens-1]
                seg_name, seg_ext = os.path.splitext(img_name)
                n_len = len(seg_name)
                img_name = seg_name[:n_len-2] + seg_ext
                list_temp.append(img_name)
                ftrs_clfrstemp = csv.writer(ftrs_clfrs)
                ftrs_clfrstemp.writerow(list_temp)
                list_temp.clear()
                curr_seg = 0
            curr_seg +=1
                    
        ftrs_clfrs.close()
        ftrs_cat.close()
        ftrs_dog.close()
        
    #HOG Features
    for dim_ppc in ['d32p8', 'd32p16', 'd32p32', 'd64p16', 'd64p32', 'd64p64', 'd128p32', 'd128p64', 'd128p128']:
        ftrspath_clfrs = options.feature_path + "4Clfrs/" + run4 + "/hog_" + dim_ppc + ".csv"
        ftrspath_cat = options.feature_path + "/" + run4 + "/cat/hogcat_" + dim_ppc + ".csv"
        ftrspath_dog = options.feature_path + "/" + run4 + "/dog/hogdog_" + dim_ppc + ".csv"
        
        ftrs_clfrs = open(ftrspath_clfrs, 'w')
        ftrs_cat = open(ftrspath_cat,'r')
        ftrs_dog = open(ftrspath_dog,'r')
        
        curr_seg = 1
        total_segs = 9
        list_temp = []
        b_writeheader = True
        for line in ftrs_cat:
            line_split = line.strip().split(',')
            n_tokens = len(line_split)
            if b_writeheader:
                ftrs_clfrs.write('CatsDog Features\n\n')
                str_temp = 'Total Features ' + str((n_tokens-1)*total_segs) + '\t' + 'class {0,1}' + '\t' +  'Image Path\n'
                ftrs_clfrs.write(str_temp)
                b_writeheader = False
                

            list_temp.extend(line_split[:n_tokens-1])
            #n_len = len(list_temp)
            if curr_seg == total_segs:
                #append the class
                list_temp.append(0)
                img_name = line_split[n_tokens-1]
                seg_name, seg_ext = os.path.splitext(img_name)
                n_len = len(seg_name)
                img_name = seg_name[:n_len-2] + seg_ext
                list_temp.append(img_name)
                ftrs_clfrstemp = csv.writer(ftrs_clfrs)
                ftrs_clfrstemp.writerow(list_temp)
                list_temp.clear()
                curr_seg = 0
            curr_seg +=1
                    
        for line in ftrs_dog:
            line_split = line.strip().split(',')
            n_tokens = len(line_split)
            list_temp.extend(line_split[:n_tokens-1])
            if curr_seg == total_segs:
                #append the class
                list_temp.append(1)
                img_name = line_split[n_tokens-1]
                seg_name, seg_ext = os.path.splitext(img_name)
                n_len = len(seg_name)
                img_name = seg_name[:n_len-2] + seg_ext
                list_temp.append(img_name)
                ftrs_clfrstemp = csv.writer(ftrs_clfrs)
                ftrs_clfrstemp.writerow(list_temp)
                list_temp.clear()
                curr_seg = 0
            curr_seg +=1
        
        ftrs_clfrs.close()
        ftrs_cat.close()
        ftrs_dog.close()
        
    #LBP Features
    for dim in [32, 64,128]:
        for radius in [2, 3, 4]:
            ftrspath_clfrs = options.feature_path + "4Clfrs/" + run4 + "/lbp_" + str(dim) + "_" + str(radius) + ".csv"
            ftrspath_cat = options.feature_path + "/" + run4 + "/cat/lbpcat_" + str(dim) + "_" + str(radius) + ".csv"
            ftrspath_dog = options.feature_path + "/" + run4 + "/dog/lbpdog_" + str(dim) + "_" + str(radius) + ".csv"
        
            ftrs_clfrs = open(ftrspath_clfrs, 'w')
            ftrs_cat = open(ftrspath_cat,'r')
            ftrs_dog = open(ftrspath_dog,'r')
            
            curr_seg = 1
            total_segs = 9
            list_temp = []
            b_writeheader = True
            for line in ftrs_cat:
                line_split = line.strip().split(',')
                n_tokens = len(line_split)
                if b_writeheader:
                    ftrs_clfrs.write('CatsDog Features\n\n')
                    str_temp = 'Total Features ' + str((n_tokens-1)*total_segs) + '\t' + 'class {0,1}' + '\t' +  'Image Path\n'
                    ftrs_clfrs.write(str_temp)
                    b_writeheader = False
                    
    
                list_temp.extend(line_split[:n_tokens-1])
                #n_len = len(list_temp)
                if curr_seg == total_segs:
                    #append the class
                    list_temp.append(0)
                    img_name = line_split[n_tokens-1]
                    seg_name, seg_ext = os.path.splitext(img_name)
                    n_len = len(seg_name)
                    img_name = seg_name[:n_len-2] + seg_ext
                    list_temp.append(img_name)
                    ftrs_clfrstemp = csv.writer(ftrs_clfrs)
                    ftrs_clfrstemp.writerow(list_temp)
                    list_temp.clear()
                    curr_seg = 0
                curr_seg +=1
                        
            for line in ftrs_dog:
                line_split = line.strip().split(',')
                n_tokens = len(line_split)
                list_temp.extend(line_split[:n_tokens-1])
                if curr_seg == total_segs:
                    #append the class
                    list_temp.append(1)
                    img_name = line_split[n_tokens-1]
                    seg_name, seg_ext = os.path.splitext(img_name)
                    n_len = len(seg_name)
                    img_name = seg_name[:n_len-2] + seg_ext
                    list_temp.append(img_name)
                    ftrs_clfrstemp = csv.writer(ftrs_clfrs)
                    ftrs_clfrstemp.writerow(list_temp)
                    list_temp.clear()
                    curr_seg = 0
                curr_seg +=1
            
            ftrs_clfrs.close()
            ftrs_cat.close()
            ftrs_dog.close()
        
        
    #GLCM Features
    for dim in [32, 64,128]:
        ftrspath_clfrs = options.feature_path + "4Clfrs/" + run4 + "/glcm_" + str(dim) + ".csv"
        ftrspath_cat = options.feature_path + "/" + run4 + "/cat/glcmcat_" + str(dim) + ".csv"
        ftrspath_dog = options.feature_path + "/" + run4 + "/dog/glcmdog_" + str(dim) + ".csv"
    
        ftrs_clfrs = open(ftrspath_clfrs, 'w')
        ftrs_cat = open(ftrspath_cat,'r')
        ftrs_dog = open(ftrspath_dog,'r')
        
        curr_seg = 1
        total_segs = 9
        list_temp = []
        b_writeheader = True
        for line in ftrs_cat:
            line_split = line.strip().split(',')
            n_tokens = len(line_split)
            if b_writeheader:
                ftrs_clfrs.write('CatsDog Features\n\n')
                str_temp = 'Total Features ' + str((n_tokens-1)*total_segs) + '\t' + 'class {0,1}' + '\t' +  'Image Path\n'
                ftrs_clfrs.write(str_temp)
                b_writeheader = False
                

            list_temp.extend(line_split[:n_tokens-1])
            #n_len = len(list_temp)
            if curr_seg == total_segs:
                #append the class
                list_temp.append(0)
                img_name = line_split[n_tokens-1]
                seg_name, seg_ext = os.path.splitext(img_name)
                n_len = len(seg_name)
                img_name = seg_name[:n_len-2] + seg_ext
                list_temp.append(img_name)
                ftrs_clfrstemp = csv.writer(ftrs_clfrs)
                ftrs_clfrstemp.writerow(list_temp)
                list_temp.clear()
                curr_seg = 0
            curr_seg +=1
                    
        for line in ftrs_dog:
            line_split = line.strip().split(',')
            n_tokens = len(line_split)
            list_temp.extend(line_split[:n_tokens-1])
            if curr_seg == total_segs:
                #append the class
                list_temp.append(1)
                img_name = line_split[n_tokens-1]
                seg_name, seg_ext = os.path.splitext(img_name)
                n_len = len(seg_name)
                img_name = seg_name[:n_len-2] + seg_ext
                list_temp.append(img_name)
                ftrs_clfrstemp = csv.writer(ftrs_clfrs)
                ftrs_clfrstemp.writerow(list_temp)
                list_temp.clear()
                curr_seg = 0
            curr_seg +=1
        
        ftrs_clfrs.close()
        ftrs_cat.close()
        ftrs_dog.close()