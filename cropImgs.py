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

parser.add_option("-p", "--path", dest="data_path", help="Path to datafile", default="data/")
parser.add_option("-c", "--class", dest="class_type", help="image class", default="Cat")
parser.add_option("-t", "--type", dest="run4", help="run for train or test", default="train")
parser.add_option("-i", "--input", dest="input_path", help="Path to input images.", default="Imgs/")
parser.add_option("-o", "--output", dest="output_path", help="Path to res file.", default="resImgs/")
parser.add_option("-s", "--seg_type", dest="seg_type", help="Segmentation type.", default="Eyes")

(options, args) = parser.parse_args()

mFile = options.data_path + "data" + options.class_type + options.seg_type + "_" + options.run4 + ".csv"


def loadMetaInfo(filePath):
    allImgs = {}

    with open(filePath, 'r') as fInput:

        print('Parsing input data file')
        bIgnr = True

        for strLine in fInput:
            # ignore the header line
            if bIgnr:
                bIgnr = False
                continue
            strTokens = strLine.strip().split(',')
            (filename,xmin,ymin,xmax,ymax,pType) = strTokens
            strId = filename

            if strId not in allImgs:
                allImgs[strId] = {}
                allImgs[strId]['strId'] = strId
                allImgs[strId]['filename'] = filename
                allImgs[strId]['xmin'] = xmin
                allImgs[strId]['ymin'] = ymin
                allImgs[strId]['xmax'] = xmax
                allImgs[strId]['ymax'] = ymax
                allImgs[strId]['pType'] = pType
            else:
                nVrsn=1
                while True:
                    strIdNew = strId + "_" + str(nVrsn)
                    if strIdNew not in allImgs:
                        allImgs[strIdNew] = {}
                        allImgs[strIdNew]['strId'] = strIdNew
                        allImgs[strIdNew]['filename'] = filename
                        allImgs[strIdNew]['xmin'] = xmin
                        allImgs[strIdNew]['ymin'] = ymin
                        allImgs[strIdNew]['xmax'] = xmax
                        allImgs[strIdNew]['ymax'] = ymax
                        allImgs[strIdNew]['pType'] = pType
                        break
    return allImgs


allImgs = loadMetaInfo(mFile)

options.input_path += options.class_type
options.output_path += options.run4 + "/" + options.class_type + "/" + options.seg_type

for strId in allImgs:
    imgInfo = allImgs[strId]
    strId = allImgs[strId]['strId']
    filename = allImgs[strId]['filename']
    xmin = int(allImgs[strId]['xmin'])
    ymin = int(allImgs[strId]['ymin'])
    xmax = int(allImgs[strId]['xmax'])
    ymax = int(allImgs[strId]['ymax'])
    pType = allImgs[strId]['pType']

    #crop the file name
    filename = filename[7:]
    filepath = options.input_path + filename
    #load img
    img = cv2.imread(filepath)

    # temp chg AB keep BBox inside the image
    (rows, cols) = img.shape[:2]
    nWidth = int(cols)
    nHeight = int(rows)
    if xmin < 0:
        xmin = int(0)
    if ymin < 0:
        ymin = int(0)
    if xmax > nWidth:
        xmax = nWidth
    if ymax > nHeight:
        ymax = nHeight
    # ~End temp chg AB

    #crop the img
    img = img[ymin:ymax, xmin:xmax]
    #cv2.rectangle(img, (nXmin, nYmin), (nXmax, nYmax), (int(255), int(60), int(60)), 2)

    strCropId, strExtId = os.path.splitext(strId)
    nLen = len(strExtId)
    strVrsn = ""
    if nLen > 4:
        strVrsn = strExtId[4:]
    filename, strExt = os.path.splitext(filename)
    filename = filename + strVrsn + strExt

    strCropImgPath = options.output_path + filename

    cv2.imwrite(strCropImgPath, img)

test = 0