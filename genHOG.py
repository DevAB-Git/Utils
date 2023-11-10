#######################################################################################################################
#
#genHOG.py
#
#######################################################################################################################
import computeHOG as chg
from optparse import OptionParser

parser = OptionParser()

parser.add_option("-f", "--feature_path", dest="feature_path", help="Path to features file", default="../MetaData/Features/")
parser.add_option("-c", "--class", dest="class_type", help="image class", default="cat")
parser.add_option("-t", "--type", dest="run4", help="run for train, test", default="train")
parser.add_option("-i", "--input", dest="input_path", help="Path to input segmented images.", default="../MetaData/Imgs/")
parser.add_option("-p", "--params", dest="dim_ppc", help="image dim and pixels_per_cell.", default="all")

(options, args) = parser.parse_args()


for run4 in ['train', 'test']:
#for run4 in ['test']:
    for class_type in ['cat', 'dog']:
    #for class_type in ['dog']:
        imgsAbstPath = options.input_path + run4 + "/" + class_type
        ftrsPath = options.feature_path + run4 + "/" + class_type + "/hog"+class_type
        #for dim_ppc in ['d64p16', 'd64p32', 'd64p64', 'd128p32', 'd128p64', 'd128p128', 'd256p64', 'd256p128', 'd256p256']:
        for dim_ppc in ['d64p4', 'd64p8', 'd64p12', 'd128p8', 'd128p16', 'd128p24', 'd256p16', 'd256p32', 'd256p48']:
            fFtrsPath = ftrsPath + "_" + dim_ppc + ".csv"
            chg.compHOG(imgsAbstPath, fFtrsPath, dim_ppc)