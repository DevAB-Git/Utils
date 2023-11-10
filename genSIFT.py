from optparse import OptionParser
import computeSIFT as cst

"""Imp Note
        patchSize: size of the patch in pixels 
        maxBinValue: maximum descriptor element after L2 normalization. All above are clipped to this value
        numOrientationBins: number of orientation bins for histogram
        numSpatialBins: number of spatial bins. The final descriptor size is numSpatialBins x numSpatialBins x numOrientationBins
        numSpatialBins = 4,3,2 , sift features will be 128, 72, and 32 respectively
        numSpatialBins is initialized in numpy_sift
"""


parser = OptionParser()

parser.add_option("-f", "--feature_path", dest="feature_path", help="Path to features file", default="../MetaData/Features/")
parser.add_option("-c", "--class", dest="class_type", help="image class, could be Cat, Dog, All", default="all")
parser.add_option("-t", "--type", dest="run4", help="run for train, prediction", default="train")
parser.add_option("-i", "--input", dest="input_path", help="Path to input segmented images.", default="../MetaData/Imgs/")
parser.add_option("-p", "--params", dest="psize_sbins", help="patch size (i.e. image dim) and numSpatialBins.", default="p64b4")

(options, args) = parser.parse_args()

if options.class_type !='all':
    imgsAbstPath = options.input_path + options.run4 + "/" + options.class_type + "/" + options.seg_type
    ftrsPath = options.feature_path + options.run4 + "/" + options.class_type + "/" + options.seg_type + \
               "/sift" + options.class_type + options.seg_type + "_" + options.psize_sbins + ".csv"

    cst.compSIFT(imgsAbstPath, ftrsPath, options.psize_sbins)
else:
    for run4 in ['train', 'test']:
        for class_type in ['cat', 'dog']:
            #for psize_sbins in ['p64b4', 'p64b3', 'p64b2', 'p128b4', 'p128b3', 'p128b2', 'p256b4', 'p256b3', 'p256b2']:
            for psize_sbins in ['p64b7', 'p64b6', 'p64b5', 'p128b7', 'p128b6', 'p128b5', 'p256b7', 'p256b6', 'p256b5']:
                imgsAbstPath = options.input_path + run4 + "/" + class_type
                ftrsPath = options.feature_path + run4 + "/" + class_type + "/"+ "sift" + class_type + "_" + psize_sbins + ".csv"

                cst.compSIFT(imgsAbstPath, ftrsPath, psize_sbins)

test =0
