import os
import cv2

from numpy_sift import SIFTDescriptor

def compSIFT(imgsPath, fFtrsPath, psize_sbins):
    nPSize, nSBins = getPSizeSBins(psize_sbins)
    fFtrsSIFT = open(fFtrsPath, 'w')

    for idxClass, imgName in enumerate(sorted(os.listdir(imgsPath))):
        if not imgName.lower().endswith(('.bmp', '.jpeg', '.jpg', '.png', '.tif', '.tiff')):
            continue

        imgNameOrg = imgName
        filepath = os.path.join(imgsPath, imgName)
        ##############################################################
        img = cv2.imread(filepath, 0)
        img = cv2.resize(img, (nPSize, nPSize))
        h, w = img.shape

        SD = SIFTDescriptor(patchSize=nPSize, numSpatialBins=nSBins)

        patch = img[0: nPSize, 0: nPSize]
        h1, w1 = patch.shape

        sift = SD.describe(patch)

        #################################################################
        strFd = ""
        for fdTemp in sift:
            strFd = strFd + ("{0:.4f}".format(fdTemp)) + ","
        strFd += filepath + "\n"
        # fHog.write(imgName, imgClass)
        fFtrsSIFT.write(strFd)

        test = 0

    fFtrsSIFT.close()

def getPSizeSBins(psize_sbins):
    nIdx = psize_sbins.find('b')
    nPSize = int(psize_sbins[1:nIdx])
    nIdx+=1
    nSBins = int(psize_sbins[nIdx:])

    return nPSize, nSBins
