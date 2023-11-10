import os
import cv2
import lbp
##############################
# See notes at the end
##############################
def compLBP(imgsPath, fFtrsPath, dim, n_points, radius):
    # initialize the local binary patterns descriptor
    lbp_desc = lbp.LocalBinaryPatterns(n_points, radius)
    ftrs_lbp = open(fFtrsPath, 'w')
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
        lbp_hist = lbp_desc.describe(img_gray)
        
        n_lbp = len(lbp_hist)
        strFd = ""
        for fdTemp in lbp_hist:
            strFd = strFd + ("{0:.4f}".format(fdTemp)) + ","
        strFd += filepath + "\n"
        # fHog.write(imgName, imgClass)
        ftrs_lbp.write(strFd)
    
    ftrs_lbp.close()
'''
###############################
#Imp AB note
#total lbp features with uniform settings will be
#num_patterns = samples + 2 i.e. lbp_featurs = n_points +2

# initialize the local binary patterns descriptor
radius = 3
n_points = 8 * radius
#desc = lbp.LocalBinaryPatterns(24, 8)
desc = lbp.LocalBinaryPatterns(n_points, radius)
# load the image, convert it to grayscale, and describe it
#dimImg = (256, 256)
dimImg_0 = (256, 256)
dimImg_1 = (128, 128)
dimImg_2 = (64, 64)

filepath = '../MetaData/CatsDog/Imgs/train/cat/000000001_000.jpg'
img_org = cv2.imread(filepath)

img = cv2.resize(img_org, dimImg_0)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist = desc.describe(gray)
n_size = len(hist)
print(n_size)
img = cv2.resize(img_org, dimImg_1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist = desc.describe(gray)
n_size = len(hist)
print(n_size)

img = cv2.resize(img_org, dimImg_2)
h1, w1 = img.shape[:2]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist = desc.describe(gray)
n_size = len(hist)
print(n_size)
temp = 0
#############################################
'''
