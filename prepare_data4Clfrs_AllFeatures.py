import os
import shutil
import re
import numpy as np
import csv
from optparse import OptionParser

parser = OptionParser()

parser.add_option("-f", "--feature_path", dest="feature_path", help="Path to features file", default="../MetaData/Features")

(options, args) = parser.parse_args()


for run4 in ['train', 'test']:
    #SIFT, HOG, LBP, GLCM Features
    #for sift_hog_lbp_d in ['p64b4_d64p16_r4_d64', 'p64b3_d64p32_r3_d64', 'p64b2_d64p64_r2_d64', 'p128b4_d128p32_r4_d128', 'p128b3_d128p64_r3_d128', 'p128b2_d128p128_r2_d128', 'p256b4_d256p64_r4_d256', 'p256b3_d256p128_r3_d256', 'p256b2_d256p256_r2_d256']:
    for sift_hog_lbp_d in ['p256b4_d256p32_r4_d256']:
        #n_cnt = sift_hog_lbp_d.count('_')
        cnj_pt = sift_hog_lbp_d.find('_')
        psize_sbins = sift_hog_lbp_d[:cnj_pt]
        hog_lbp_d = sift_hog_lbp_d[cnj_pt+1:]
        cnj_pt = hog_lbp_d.find('_')
        dim_ppc = hog_lbp_d[:cnj_pt]
        lbp_d = hog_lbp_d[cnj_pt+1:]
        cnj_pt = lbp_d.find('_')
        radius = lbp_d[1:cnj_pt]
        dim = lbp_d[cnj_pt+2:]
        
        ftrspath_clfrs = options.feature_path + "4Clfrs/" + run4 + "/sift_" + psize_sbins + "_hog_" + dim_ppc + "_lbp_r" + radius + "_dim_" + dim + ".csv"
        ftrspath_cat_sift = options.feature_path + "/" + run4 + "/cat/siftcat_" + psize_sbins + ".csv"
        ftrspath_dog_sift = options.feature_path + "/" + run4 + "/dog/siftdog_" + psize_sbins + ".csv"
        ftrspath_cat_hog = options.feature_path + "/" + run4 + "/cat/hogcat_" + dim_ppc + ".csv"
        ftrspath_dog_hog = options.feature_path + "/" + run4 + "/dog/hogdog_" + dim_ppc + ".csv"
        ftrspath_cat_lbp = options.feature_path + "/" + run4 + "/cat/lbpcat_" + dim + '_' + radius + ".csv"
        ftrspath_dog_lbp = options.feature_path + "/" + run4 + "/dog/lbpdog_" + dim + '_' + radius + ".csv"
        ftrspath_cat_glcm = options.feature_path + "/" + run4 + "/cat/glcmcat_" + dim + ".csv"
        ftrspath_dog_glcm = options.feature_path + "/" + run4 + "/dog/glcmdog_" + dim + ".csv"
        
        ftrs_clfrs = open(ftrspath_clfrs, 'w')
        ftrs_cat_sift = open(ftrspath_cat_sift,'r')
        ftrs_dog_sift = open(ftrspath_dog_sift,'r')
        ftrs_cat_hog = open(ftrspath_cat_hog,'r')
        ftrs_dog_hog = open(ftrspath_dog_hog,'r')
        ftrs_cat_lbp = open(ftrspath_cat_lbp,'r')
        ftrs_dog_lbp = open(ftrspath_dog_lbp,'r')
        ftrs_cat_glcm = open(ftrspath_cat_glcm,'r')
        ftrs_dog_glcm = open(ftrspath_dog_glcm,'r')
        
        #Read all files
        lines_cat_sift = ftrs_cat_sift.readlines()
        lines_dog_sift =  ftrs_dog_sift.readlines()
        lines_cat_hog = ftrs_cat_hog.readlines()
        lines_dog_hog =  ftrs_dog_hog.readlines()
        lines_cat_lbp = ftrs_cat_lbp.readlines()
        lines_dog_lbp =  ftrs_dog_lbp.readlines()
        lines_cat_glcm = ftrs_cat_glcm.readlines()
        lines_dog_glcm =  ftrs_dog_glcm.readlines()
        
        assert((len(lines_cat_sift) == len(lines_cat_hog)) and (len(lines_cat_sift) == len(lines_cat_lbp)) and (len(lines_cat_sift) == len(lines_cat_glcm)))
        assert((len(lines_dog_sift) == len(lines_dog_hog)) and (len(lines_dog_sift) == len(lines_dog_lbp)) and (len(lines_dog_sift) == len(lines_dog_glcm)))
        
        #Cats Features
        b_writeheader = True
        for line_sift, line_hog, line_lbp, line_glcm in zip(lines_cat_sift, lines_cat_hog, lines_cat_lbp, lines_cat_glcm):
            line_split_sift = line_sift.strip().split(',')
            line_split_hog = line_hog.strip().split(',')
            line_split_lbp = line_lbp.strip().split(',')
            line_split_glcm = line_glcm.strip().split(',')
            n_tokens_sift = len(line_split_sift)
            n_tokens_hog = len(line_split_hog)
            n_tokens_lbp = len(line_split_lbp)
            n_tokens_glcm = len(line_split_glcm)
            
            if b_writeheader:
                ftrs_clfrs.write('CatsDog Features\n\n')
                str_temp = 'Total Features ' + str(n_tokens_sift + n_tokens_hog + n_tokens_lbp + n_tokens_glcm -4) + '\t' + '(SIFT ' + str(n_tokens_sift-1) + ', HOG ' + str(n_tokens_hog-1) + ', LBP ' + str(n_tokens_lbp-1) +', GLCM ' + str(n_tokens_glcm-1) + ')\t' + 'class {0,1}' + '\t' +  'Image Path\n'
                ftrs_clfrs.write(str_temp)
                b_writeheader = False
            
            list_temp = line_split_sift[:n_tokens_sift-1]
            list_temp.extend(line_split_hog[:n_tokens_hog-1])            
            list_temp.extend(line_split_lbp[:n_tokens_lbp-1])
            list_temp.extend(line_split_glcm[:n_tokens_glcm-1])
            
            temp_ab = line_split_sift[n_tokens_sift-1]
            temp_ab2 = line_split_hog[n_tokens_hog-1]
            #assert(line_split_sift[n_tokens_sift-1] == line_split_hog[n_tokens_hog-1])
            list_temp.append(0)
            list_temp.append(line_split_sift[n_tokens_sift-1])
            
            ftrs_clfrstemp = csv.writer(ftrs_clfrs)
            ftrs_clfrstemp.writerow(list_temp)
            
        #DOG Features
        for line_sift, line_hog, line_lbp, line_glcm in zip(lines_dog_sift, lines_dog_hog, lines_dog_lbp, lines_dog_glcm):
            line_split_sift = line_sift.strip().split(',')
            line_split_hog = line_hog.strip().split(',')
            line_split_lbp = line_lbp.strip().split(',')
            line_split_glcm = line_glcm.strip().split(',')
            n_tokens_sift = len(line_split_sift)
            n_tokens_hog = len(line_split_hog)
            n_tokens_lbp = len(line_split_lbp)
            n_tokens_glcm = len(line_split_glcm)
                       
            list_temp = line_split_sift[:n_tokens_sift-1]
            list_temp.extend(line_split_hog[:n_tokens_hog-1])            
            list_temp.extend(line_split_lbp[:n_tokens_lbp-1])
            list_temp.extend(line_split_glcm[:n_tokens_glcm-1])
            
            #assert(line_split_sift[n_tokens_sift-1] == line_split_hog[n_tokens_hog-1])
            list_temp.append(1)
            list_temp.append(line_split_sift[n_tokens_sift-1])
            
            ftrs_clfrstemp = csv.writer(ftrs_clfrs)
            ftrs_clfrstemp.writerow(list_temp)
        
        
        #close all the files
        ftrs_clfrs.close()
        ftrs_cat_sift.close()
        ftrs_dog_sift.close()
        ftrs_cat_hog.close()
        ftrs_dog_hog.close()    
        
        