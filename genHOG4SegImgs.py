#######################################################################################################################
#
#genHOG.py
#
#######################################################################################################################
import computeHOG as chg
from optparse import OptionParser

parser = OptionParser()

parser.add_option("-f", "--feature_path", dest="feature_path", help="Path to features file", default="../MetaData/CatsDog/SegFeatures/")
#parser.add_option("-c", "--class", dest="class_type", help="image class", default="cat")
#parser.add_option("-t", "--type", dest="run4", help="run for train, test", default="train")
parser.add_option("-i", "--input", dest="input_path", help="Path to input segmented images.", default="../MetaData/CatsDog/SegImgs/")
parser.add_option("-p", "--params", dest="dim_ppc", help="image dim and pixels_per_cell.", default="all")

(options, args) = parser.parse_args()

#imgsAbstPath = options.input_path + options.run4 + "/" + options.class_type
#ftrsPath = options.feature_path + options.run4 + "/" + options.class_type + "/" +\
#            "/hog"+options.class_type

for run4 in ['train', 'test']:
        for class_type in ['cat', 'dog']:
            
            imgsAbstPath = options.input_path + run4 + "/" + class_type
            ftrsPath = options.feature_path + run4 + "/" + class_type + \
                        "/hog"+class_type
            if options.dim_ppc != 'all':
                fFtrsPath = ftrsPath + "_" + options.dim_ppc + ".csv"
                chg.compHOG(imgsAbstPath, fFtrsPath, options.dim_ppc)
            else:
                for dim_ppc in ['d32p8', 'd32p16', 'd32p32', 'd64p16', 'd64p32', 'd64p64', 'd128p32', 'd128p64', 'd128p128']:
                    fFtrsPath = ftrsPath + "_" + dim_ppc + ".csv"
                    chg.compHOG(imgsAbstPath, fFtrsPath, dim_ppc)