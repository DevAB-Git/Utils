import os
import shutil
import re
import numpy as np
import csv
from optparse import OptionParser

parser = OptionParser()

parser.add_option("-f", "--feature_path", dest="feature_path", help="Path to features file", default="../MetaData/CatsDog/SegFeatures")

(options, args) = parser.parse_args()


for run4 in ['train', 'test']:
    #SIFT_HOG Features
    for sift_hog in ['p32b4_d32p8', 'p32b3_d32p16', 'p32b2_d32p32', 'p64b4_d64p16', 'p64b3_d64p32', 'p64b2_d64p64', 'p128b4_d128p32', 'p128b3_d128p64', 'p128b2_d128p128' ]:
        cnj_pt = sift_hog.find('_')
        psize_sbins = sift_hog[:cnj_pt]
        dim_ppc = sift_hog[cnj_pt+1:]
        
        ftrspath_ucs = options.feature_path + "4UCS/" + run4 + "/sift_" + psize_sbins + "_hog_" + dim_ppc + ".csv"
        ftrspath_cat_sift = options.feature_path + "/" + run4 + "/cat/siftcat_" + psize_sbins + ".csv"
        ftrspath_dog_sift = options.feature_path + "/" + run4 + "/dog/siftdog_" + psize_sbins + ".csv"
        ftrspath_cat_hog = options.feature_path + "/" + run4 + "/cat/hogcat_" + dim_ppc + ".csv"
        ftrspath_dog_hog = options.feature_path + "/" + run4 + "/dog/hogdog_" + dim_ppc + ".csv"
        
        ftrs_ucs = open(ftrspath_ucs, 'w')
        ftrs_cat_sift = open(ftrspath_cat_sift,'r')
        ftrs_dog_sift = open(ftrspath_dog_sift,'r')
        ftrs_cat_hog = open(ftrspath_cat_hog,'r')
        ftrs_dog_hog = open(ftrspath_dog_hog,'r')
        
        #Read all files
        lines_cat_sift = ftrs_cat_sift.readlines()
        lines_dog_sift =  ftrs_dog_sift.readlines()
        lines_cat_hog = ftrs_cat_hog.readlines()
        lines_dog_hog =  ftrs_dog_hog.readlines()
        
        assert(len(lines_cat_sift) == len(lines_cat_hog))
        assert(len(lines_dog_sift) == len(lines_dog_hog))
        
        b_writeheader = True
        curr_seg = 1
        total_segs = 9
        list_temp = []
        
        for line_sift, line_hog in zip(lines_cat_sift, lines_cat_hog):
            line_split_sift = line_sift.strip().split(',')
            line_split_hog = line_hog.strip().split(',')
            n_tokens_sift = len(line_split_sift)
            n_tokens_hog = len(line_split_hog)
            if b_writeheader:
                ftrs_ucs.write('@relation imgs\n\n')
                ftr_no = 0
                total_ftrs = (n_tokens_sift-1)*total_segs
                for i in range(total_ftrs):
                    str_temp = '@ATTRIBUTE' + '\t' + 'F' + str(ftr_no) + '\t' + 'REAL\n'
                    ftrs_ucs.write(str_temp)
                    ftr_no+=1
                total_ftrs = (n_tokens_hog-1)*total_segs
                for i in range(total_ftrs):
                    str_temp = '@ATTRIBUTE' + '\t' + 'F' + str(ftr_no) + '\t' + 'REAL\n'
                    ftrs_ucs.write(str_temp)
                    ftr_no+=1
                
                str_temp = '@ATTRIBUTE' + '\t' + 'class' + '\t' + '{0,1}\n'
                ftrs_ucs.write(str_temp)
                ftrs_ucs.write('\n@DATA\n')
                b_writeheader = False
            
            list_temp.extend(line_split_sift[:n_tokens_sift-1])
            list_temp.extend(line_split_hog[:n_tokens_hog-1])
            
            if curr_seg == total_segs:
                #append the class
                list_temp.append(0)
                assert(line_split_sift[n_tokens_sift-1] == line_split_hog[n_tokens_hog-1])
                img_name = line_split_sift[n_tokens_sift-1]
                seg_name, seg_ext = os.path.splitext(img_name)
                n_len = len(seg_name)
                img_name = seg_name[:n_len-2] + seg_ext
                list_temp.append(img_name)
                ftrs_ucstemp = csv.writer(ftrs_ucs)
                ftrs_ucstemp.writerow(list_temp)
                list_temp.clear()
                curr_seg = 0
            curr_seg +=1
        
        for line_sift, line_hog in zip(lines_dog_sift, lines_dog_hog):
            line_split_sift = line_sift.strip().split(',')
            line_split_hog = line_hog.strip().split(',')
            n_tokens_sift = len(line_split_sift)
            n_tokens_hog = len(line_split_hog)
            
            list_temp.extend(line_split_sift[:n_tokens_sift-1])
            list_temp.extend(line_split_hog[:n_tokens_hog-1])
            
            if curr_seg == total_segs:
                #append the class
                list_temp.append(1)
                assert(line_split_sift[n_tokens_sift-1] == line_split_hog[n_tokens_hog-1])
                img_name = line_split_sift[n_tokens_sift-1]
                seg_name, seg_ext = os.path.splitext(img_name)
                n_len = len(seg_name)
                img_name = seg_name[:n_len-2] + seg_ext
                list_temp.append(img_name)
                ftrs_ucstemp = csv.writer(ftrs_ucs)
                ftrs_ucstemp.writerow(list_temp)
                list_temp.clear()
                curr_seg = 0
            curr_seg +=1
        
                
        
        #close all the files
        ftrs_ucs.close()
        ftrs_cat_sift.close()
        ftrs_dog_sift.close()
        ftrs_cat_hog.close()
        ftrs_dog_hog.close()