import os
import cv2
import numpy as np
import skimage.feature as feature


def computeGLCM(imgsPath, fFtrsPath, dim):
    ftrs_glcm = open(fFtrsPath, 'w')
    dim_img = (dim, dim)
    for idxClass, imgName in enumerate(sorted(os.listdir(imgsPath))):
        if not imgName.lower().endswith(('.bmp', '.jpeg', '.jpg', '.png', '.tif', '.tiff')):
            continue

        imgNameOrg = imgName
        filepath = os.path.join(imgsPath, imgName)
        img = cv2.imread(filepath)
        #h1, w1 = img.shape[:2]
        img = cv2.resize(img, dim_img)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        graycom = feature.graycomatrix(img_gray, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], levels=256)
        glcm_ftrs = []        
        glcm_ftrs.extend(feature.graycoprops(graycom, 'contrast')[0])
        glcm_ftrs.extend(feature.graycoprops(graycom, 'dissimilarity')[0])
        glcm_ftrs.extend(feature.graycoprops(graycom, 'homogeneity')[0])
        glcm_ftrs.extend(feature.graycoprops(graycom, 'energy')[0])
        glcm_ftrs.extend(feature.graycoprops(graycom, 'correlation')[0])
        glcm_ftrs.extend(feature.graycoprops(graycom, 'ASM')[0])
        strFd = ""
        for fdTemp in glcm_ftrs:
            strFd = strFd + ("{0:.4f}".format(fdTemp)) + ","
        strFd += filepath + "\n"
        # fHog.write(imgName, imgClass)
        ftrs_glcm.write(strFd)
        
    ftrs_glcm.close()
#####################################################################
'''
filepath = 'sample.jpg'
img = cv2.imread(filepath)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Param:
# source image
# List of pixel pair distance offsets - here 1 in each direction
# List of pixel pair angles in radians
graycom = feature.graycomatrix(img_gray, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], levels=256)
glcm_ftrs=[]
contrast = feature.graycoprops(graycom, 'contrast')
glcm_ftrs.extend(feature.graycoprops(graycom, 'contrast')[0])
dissimilarity = feature.graycoprops(graycom, 'dissimilarity')
glcm_ftrs.extend(feature.graycoprops(graycom, 'dissimilarity')[0])
homogeneity = feature.graycoprops(graycom, 'homogeneity')
glcm_ftrs.extend(feature.graycoprops(graycom, 'homogeneity')[0])
energy = feature.graycoprops(graycom, 'energy')
glcm_ftrs.extend(feature.graycoprops(graycom, 'energy')[0])
correlation = feature.graycoprops(graycom, 'correlation')
glcm_ftrs.extend(feature.graycoprops(graycom, 'correlation')[0])
ASM = feature.graycoprops(graycom, 'ASM')
glcm_ftrs.extend(feature.graycoprops(graycom, 'ASM')[0])

# Find the GLCM properties
contrast = feature.graycoprops(graycom, 'contrast')
dissimilarity = feature.graycoprops(graycom, 'dissimilarity')
homogeneity = feature.graycoprops(graycom, 'homogeneity')
energy = feature.graycoprops(graycom, 'energy')
correlation = feature.graycoprops(graycom, 'correlation')
ASM = feature.graycoprops(graycom, 'ASM')
print("Contrast: {}".format(contrast))
print("Dissimilarity: {}".format(dissimilarity))
print("Homogeneity: {}".format(homogeneity))
print("Energy: {}".format(energy))
print("Correlation: {}".format(correlation))
print("ASM: {}".format(ASM))
'''
