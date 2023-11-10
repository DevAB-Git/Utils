from optparse import OptionParser
import computeGLCM as cglcm

parser = OptionParser()

parser.add_option("-f", "--feature_path", dest="feature_path", help="Path to features file", default="../MetaData/CatsDog/Features/")
parser.add_option("-c", "--class", dest="class_type", help="image class, could be Cat, Dog, All", default="all")
parser.add_option("-t", "--type", dest="run4", help="run for train, prediction", default="train")
parser.add_option("-i", "--input", dest="input_path", help="Path to input segmented images.", default="../MetaData/CatsDog/Imgs/")
parser.add_option("-d", "--dim", dest="dim", help="image size", default=128)

(options, args) = parser.parse_args()
for run4 in ['train', 'test']:
    for class_type in ['cat', 'dog']:
        for dim in [64,128,256]:
            imgsAbstPath = options.input_path + run4 + "/" + class_type
            ftrsPath = options.feature_path + run4 + "/" + class_type + "/"+ "glcm" + class_type + "_" + str(dim) +".csv"

            cglcm.computeGLCM(imgsAbstPath, ftrsPath, dim)

    
test =0
