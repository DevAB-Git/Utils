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
    #SFTI features
    for psize_sbins in ['p32b4', 'p32b3', 'p32b2', 'p64b4', 'p64b3', 'p64b2', 'p128b4', 'p128b3', 'p128b2']:
        ftrspath_ucs = options.feature_path + "4UCS/" + run4 + "/sift_" + psize_sbins + ".csv"
        ftrspath_cat = options.feature_path + "/" + run4 + "/cat/siftcat_" + psize_sbins + ".csv"
        ftrspath_dog = options.feature_path + "/" + run4 + "/dog/siftdog_" + psize_sbins + ".csv"
        
        ftrs_ucs = open(ftrspath_ucs, 'w')
        ftrs_cat = open(ftrspath_cat,'r')
        ftrs_dog = open(ftrspath_dog,'r')
        
        b_writeheader = True
        curr_seg = 1
        total_segs = 9
        list_temp = []
        for line in ftrs_cat:
            line_split = line.strip().split(',')
            n_tokens = len(line_split)
            if b_writeheader:
                ftrs_ucs.write('@relation imgs\n\n')
                total_ftrs = (n_tokens-1)*total_segs
                for i in range(total_ftrs):
                    str_temp = '@ATTRIBUTE' + '\t' + 'F' + str(i) + '\t' + 'REAL\n'
                    ftrs_ucs.write(str_temp)
                
                str_temp = '@ATTRIBUTE' + '\t' + 'class' + '\t' + '{0,1}\n'
                ftrs_ucs.write(str_temp)
                ftrs_ucs.write('\n@DATA\n')
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
                ftrs_ucstemp = csv.writer(ftrs_ucs)
                ftrs_ucstemp.writerow(list_temp)
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
                ftrs_ucstemp = csv.writer(ftrs_ucs)
                ftrs_ucstemp.writerow(list_temp)
                list_temp.clear()
                curr_seg = 0
            curr_seg +=1
        
        ftrs_ucs.close()
        ftrs_cat.close()
        ftrs_dog.close()
        
    #HOG Features
    for dim_ppc in ['d32p8', 'd32p16', 'd32p32', 'd64p16', 'd64p32', 'd64p64', 'd128p32', 'd128p64', 'd128p128']:
        ftrspath_ucs = options.feature_path + "4UCS/" + run4 + "/hog_" + dim_ppc + ".csv"
        ftrspath_cat = options.feature_path + "/" + run4 + "/cat/hogcat_" + dim_ppc + ".csv"
        ftrspath_dog = options.feature_path + "/" + run4 + "/dog/hogdog_" + dim_ppc + ".csv"
        
        ftrs_ucs = open(ftrspath_ucs, 'w')
        ftrs_cat = open(ftrspath_cat,'r')
        ftrs_dog = open(ftrspath_dog,'r')
        
        b_writeheader = True
        curr_seg = 1
        total_segs = 9
        list_temp = []
        for line in ftrs_cat:
            line_split = line.strip().split(',')
            n_tokens = len(line_split)
            if b_writeheader:
                ftrs_ucs.write('@relation imgs\n\n')
                total_ftrs = (n_tokens-1)*total_segs
                for i in range(total_ftrs):
                    str_temp = '@ATTRIBUTE' + '\t' + 'F' + str(i) + '\t' + 'REAL\n'
                    ftrs_ucs.write(str_temp)
                
                str_temp = '@ATTRIBUTE' + '\t' + 'class' + '\t' + '{0,1}\n'
                ftrs_ucs.write(str_temp)
                ftrs_ucs.write('\n@DATA\n')
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
                ftrs_ucstemp = csv.writer(ftrs_ucs)
                ftrs_ucstemp.writerow(list_temp)
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
                ftrs_ucstemp = csv.writer(ftrs_ucs)
                ftrs_ucstemp.writerow(list_temp)
                list_temp.clear()
                curr_seg = 0
            curr_seg +=1
        
        ftrs_ucs.close()
        ftrs_cat.close()
        ftrs_dog.close()
        

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