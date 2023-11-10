
import os
import cv2
from skimage.feature import hog

def compHOG(imgsPath, fFtrsPath, dim_ppc):
    dimImg, pixPrCell = getDimPPC(dim_ppc)
    fFtrsHog = open(fFtrsPath, 'w')

    for idxClass, imgName in enumerate(sorted(os.listdir(imgsPath))):
        if not imgName.lower().endswith(('.bmp', '.jpeg', '.jpg', '.png', '.tif', '.tiff')):
            continue

        imgNameOrg = imgName
        filepath = os.path.join(imgsPath, imgName)
        img = cv2.imread(filepath)
        #h1, w1 = img.shape[:2]
        img = cv2.resize(img, dimImg)
        #h2, w2 = img.shape[:2]

        # fd, hog_image = hog(img, orientations=8, pixels_per_cell=(16, 16),
        #                    cells_per_block=(1, 1), visualize=True, multichannel=True)
        fd, hog_image = hog(img, orientations=8, pixels_per_cell=pixPrCell,
                            cells_per_block=(1, 1), visualize=True, multichannel=True)

        # height, width, channels = img.shape
        # height1, width1 = hog_image.shape
        nHogs = len(fd)
        strFd = ""
        for fdTemp in fd:
            strFd = strFd + ("{0:.4f}".format(fdTemp)) + ","
        strFd += filepath + "\n"
        # fHog.write(imgName, imgClass)
        fFtrsHog.write(strFd)

        test = 0

    fFtrsHog.close()

def getDimPPC(dim_ppc):
    nIdx = dim_ppc.find('p')
    n_dim = int(dim_ppc[1:nIdx])
    nIdx+=1
    n_pix = int(dim_ppc[nIdx:])
    dimImg = (n_dim, n_dim)
    pixPrCell = (n_pix, n_pix)
    return dimImg, pixPrCell

'''
def getDimPPC(dim_ppc):
    if dim_ppc == 'd32p8':
        dimImg = (32, 32)
        pixPrCell = (8, 8)
    elif dim_ppc == 'd32p16':
        dimImg = (32, 32)
        pixPrCell = (16, 16)
    elif dim_ppc == 'd32p32':
        dimImg = (32, 32)
        pixPrCell = (32, 32)
    elif dim_ppc == 'd64p16':
        dimImg = (64, 64)
        pixPrCell = (16, 16)
    elif dim_ppc == 'd64p32':
        dimImg = (64, 64)
        pixPrCell = (32, 32)
    elif dim_ppc == 'd64p64':
        dimImg = (64, 64)
        pixPrCell = (64, 64)
    elif dim_ppc == 'd128p32':
        dimImg = (128, 128)
        pixPrCell = (32, 32)
    elif dim_ppc == 'd128p64':
        dimImg = (128, 128)
        pixPrCell = (64, 64)
    elif dim_ppc == 'd128p128':
        dimImg = (128, 128)
        pixPrCell = (128, 128)
    elif dim_ppc == 'd256p64':
        dimImg = (256, 256)
        pixPrCell = (64, 64)
    elif dim_ppc == 'd256p128':
        dimImg = (256, 256)
        pixPrCell = (128, 128)
    elif dim_ppc == 'd256p256':
        dimImg = (256, 256)
        pixPrCell = (256, 256)
    else:
        print("invalid options.dim_ppc")
        exit(1)

    return dimImg, pixPrCell
    
'''