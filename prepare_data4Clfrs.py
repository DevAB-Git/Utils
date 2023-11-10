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
    
    #SFTI features
    #for psize_sbins in ['p64b4', 'p64b3', 'p64b2', 'p128b4', 'p128b3', 'p128b2', 'p256b4', 'p256b3', 'p256b2']:
    for psize_sbins in ['p64b7', 'p64b6', 'p64b5', 'p128b7', 'p128b6', 'p128b5', 'p256b7', 'p256b6', 'p256b5']:
        ftrspath_clfrs = options.feature_path + "4Clfrs/" + run4 + "/sift_" + psize_sbins + ".csv"
        ftrspath_cat = options.feature_path + "/" + run4 + "/cat/siftcat_" + psize_sbins + ".csv"
        ftrspath_dog = options.feature_path + "/" + run4 + "/dog/siftdog_" + psize_sbins + ".csv"
        
        ftrs_clfrs = open(ftrspath_clfrs, 'w')
        ftrs_cat = open(ftrspath_cat,'r')
        ftrs_dog = open(ftrspath_dog,'r')
        
        b_writeheader = True
        for line in ftrs_cat:
            line_split = line.strip().split(',')
            n_tokens = len(line_split)
            if b_writeheader:
                ftrs_clfrs.write('CatsDog Features\n\n')
                str_temp = 'Total Features ' + str(n_tokens-1) + '\t' + 'class {0,1}' + '\t' +  'Image Path\n'
                ftrs_clfrs.write(str_temp)
                b_writeheader = False
                

            list_temp = line_split[:n_tokens-1]
            list_temp.append(0)
            list_temp.append(line_split[n_tokens-1])
            
            ftrs_clfrstemp = csv.writer(ftrs_clfrs)
            ftrs_clfrstemp.writerow(list_temp)
        
        for line in ftrs_dog:
            line_split = line.strip().split(',')
            n_tokens = len(line_split)
            list_temp = line_split[:n_tokens-1]
            list_temp.append(1)
            list_temp.append(line_split[n_tokens-1])
            
            ftrs_clfrstemp = csv.writer(ftrs_clfrs)
            ftrs_clfrstemp.writerow(list_temp)
        
        ftrs_clfrs.close()
        ftrs_cat.close()
        ftrs_dog.close()
        
    #HOG Features
    #for dim_ppc in ['d64p16', 'd64p32', 'd64p64', 'd128p32', 'd128p64', 'd128p128', 'd256p64', 'd256p128', 'd256p256']:
    for dim_ppc in ['d64p4', 'd64p8', 'd64p12', 'd128p8', 'd128p16', 'd128p24', 'd256p16', 'd256p32', 'd256p48']:
        ftrspath_clfrs = options.feature_path + "4Clfrs/" + run4 + "/hog_" + dim_ppc + ".csv"
        ftrspath_cat = options.feature_path + "/" + run4 + "/cat/hogcat_" + dim_ppc + ".csv"
        ftrspath_dog = options.feature_path + "/" + run4 + "/dog/hogdog_" + dim_ppc + ".csv"
        
        ftrs_clfrs = open(ftrspath_clfrs, 'w')
        ftrs_cat = open(ftrspath_cat,'r')
        ftrs_dog = open(ftrspath_dog,'r')
        
        b_writeheader = True
        n_tokens = -1
        for line in ftrs_cat:
            line_split = line.strip().split(',')
            n_tokens = len(line_split)
            if b_writeheader:
                ftrs_clfrs.write('CatsDog Features\n\n')
                str_temp = 'Total Features ' + str(n_tokens-1) + '\t' + 'class {0,1}' + '\t' +  'Image Path\n'
                ftrs_clfrs.write(str_temp)
                b_writeheader = False
                

            list_temp = line_split[:n_tokens-1]
            list_temp.append(0)
            list_temp.append(line_split[n_tokens-1])
            
            ftrs_clfrstemp = csv.writer(ftrs_clfrs)
            ftrs_clfrstemp.writerow(list_temp)
        
        for line in ftrs_dog:
            line_split = line.strip().split(',')
            n_tokens = len(line_split)
            list_temp = line_split[:n_tokens-1]
            list_temp.append(1)
            list_temp.append(line_split[n_tokens-1])
            
            ftrs_clfrstemp = csv.writer(ftrs_clfrs)
            ftrs_clfrstemp.writerow(list_temp)
        
        ftrs_clfrs.close()
        ftrs_cat.close()
        ftrs_dog.close()
        
    #LBP Features
    for dim in [64,128,256]:
        #for radius in [2, 3, 4]:
        for radius in [5, 6, 7]:
            ftrspath_clfrs = options.feature_path + "4Clfrs/" + run4 + "/lbp_" + str(dim) + "_" + str(radius) + ".csv"
            ftrspath_cat = options.feature_path + "/" + run4 + "/cat/lbpcat_" + str(dim) + "_" + str(radius) + ".csv"
            ftrspath_dog = options.feature_path + "/" + run4 + "/dog/lbpdog_" + str(dim) + "_" + str(radius) + ".csv"
        
            ftrs_clfrs = open(ftrspath_clfrs, 'w')
            ftrs_cat = open(ftrspath_cat,'r')
            ftrs_dog = open(ftrspath_dog,'r')
            
            b_writeheader = True
            n_tokens = -1
            for line in ftrs_cat:
                line_split = line.strip().split(',')
                n_tokens = len(line_split)
                if b_writeheader:
                    ftrs_clfrs.write('CatsDog Features\n\n')
                    str_temp = 'Total Features ' + str(n_tokens-1) + '\t' + 'class {0,1}' + '\t' +  'Image Path\n'
                    ftrs_clfrs.write(str_temp)
                    b_writeheader = False
                    
    
                list_temp = line_split[:n_tokens-1]
                list_temp.append(0)
                list_temp.append(line_split[n_tokens-1])
                
                ftrs_clfrstemp = csv.writer(ftrs_clfrs)
                ftrs_clfrstemp.writerow(list_temp)
            
            for line in ftrs_dog:
                line_split = line.strip().split(',')
                n_tokens = len(line_split)
                list_temp = line_split[:n_tokens-1]
                list_temp.append(1)
                list_temp.append(line_split[n_tokens-1])
                
                ftrs_clfrstemp = csv.writer(ftrs_clfrs)
                ftrs_clfrstemp.writerow(list_temp)
            
            ftrs_clfrs.close()
            ftrs_cat.close()
            ftrs_dog.close()
        
    '''    
    #GLCM Features
    for dim in [64,128,256]:
        ftrspath_clfrs = options.feature_path + "4Clfrs/" + run4 + "/glcm_" + str(dim) + ".csv"
        ftrspath_cat = options.feature_path + "/" + run4 + "/cat/glcmcat_" + str(dim) + ".csv"
        ftrspath_dog = options.feature_path + "/" + run4 + "/dog/glcmdog_" + str(dim) + ".csv"
    
        ftrs_clfrs = open(ftrspath_clfrs, 'w')
        ftrs_cat = open(ftrspath_cat,'r')
        ftrs_dog = open(ftrspath_dog,'r')
        
        b_writeheader = True
        n_tokens = -1
        for line in ftrs_cat:
            line_split = line.strip().split(',')
            n_tokens = len(line_split)
            if b_writeheader:
                ftrs_clfrs.write('CatsDog Features\n\n')
                str_temp = 'Total Features ' + str(n_tokens-1) + '\t' + 'class {0,1}' + '\t' +  'Image Path\n'
                ftrs_clfrs.write(str_temp)
                b_writeheader = False
                

            list_temp = line_split[:n_tokens-1]
            list_temp.append(0)
            list_temp.append(line_split[n_tokens-1])
            
            ftrs_clfrstemp = csv.writer(ftrs_clfrs)
            ftrs_clfrstemp.writerow(list_temp)
        
        for line in ftrs_dog:
            line_split = line.strip().split(',')
            n_tokens = len(line_split)
            list_temp = line_split[:n_tokens-1]
            list_temp.append(1)
            list_temp.append(line_split[n_tokens-1])
            
            ftrs_clfrstemp = csv.writer(ftrs_clfrs)
            ftrs_clfrstemp.writerow(list_temp)
        
        ftrs_clfrs.close()
        ftrs_cat.close()
        ftrs_dog.close()
    '''    
    
'''
#open the src img info file
with open(pathImgsInfo,'r') as fImgsInfo:
    b_ignr = True
    for line in fImgsInfo:
        # ignore the header line
        if b_ignr:
            b_ignr = False
            continue
        line_split = line.strip().split(',')
        (filename, x1, y1, x2, y2, class_name) = line_split
        if imgClass == "cat":
            nIdx = filename.find("CAT_0")
            chGrp = filename[nIdx+5]

        if np.random.randint(0, 6) > 0:
            newFileName = pathTrain + "/" + chGrp + filename[nIdx + 7:]
            shutil.move(filename, newFileName)
        else:
            newFileName = pathVal + "/" + chGrp + filename[nIdx + 7:]
            shutil.move(filename, newFileName)
'''