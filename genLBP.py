from optparse import OptionParser
import computeLBP as clbp

"""Imp Note
    radius = 3
    n_points = 8 * radius
    #total lbp features with uniform settings will be
    #num_patterns = samples + 2 i.e. lbp_featurs = n_points +2
"""


parser = OptionParser()

parser.add_option("-f", "--feature_path", dest="feature_path", help="Path to features file", default="../MetaData/Features/")
parser.add_option("-c", "--class", dest="class_type", help="image class, could be Cat, Dog, All", default="all")
parser.add_option("-t", "--type", dest="run4", help="run for train, prediction", default="train")
parser.add_option("-i", "--input", dest="input_path", help="Path to input segmented images.", default="../MetaData/Imgs/")
parser.add_option("-r", "--radius", dest="radius", help="radius", default=3)
parser.add_option("-d", "--dim", dest="dim", help="image size", default=128)

(options, args) = parser.parse_args()
for run4 in ['train', 'test']:
    for class_type in ['cat', 'dog']:
        for dim in [64,128,256]:
            #for radius in [2, 3, 4]:
            for radius in [5, 6, 7]:
                n_points = 8 * radius
                imgsAbstPath = options.input_path + run4 + "/" + class_type
                ftrsPath = options.feature_path + run4 + "/" + class_type + "/"+ "lbp" + class_type + "_" + str(dim) + "_" + str(radius) + ".csv"
    
                clbp.compLBP(imgsAbstPath, ftrsPath, dim, n_points, radius)

    
test =0
