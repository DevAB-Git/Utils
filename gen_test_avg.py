import os
import copy
from optparse import OptionParser
from matplotlib import streamplot


parser = OptionParser()

parser.add_option("-f", "--res_path", dest="res_path", help="Path to result files", default="../NeSI/MetaData/ExpRes/")
parser.add_option("-r", "--n_runs", dest="n_runs", help="no of runs", default=5)
parser.add_option("-n", "--common_name", dest="c_name", help="common name for output files", default="_test.txt")

(options, args) = parser.parse_args()

n_runs = options.n_runs
exp_path = options.res_path + "0"

file_path_avg = options.res_path + "avg/test_res_avg.csv"
#res_file = open(file_path, 'r')
avg_file = open(file_path_avg,'w')
    

for idxfile, file_name in enumerate(sorted(os.listdir(exp_path))):
    if not file_name.endswith(options.c_name):
        continue
    
    meta_files = []
    meta_lines_res_file = []
    
    file_path = os.path.join(exp_path, file_name)
        
    for run in range(n_runs):
        file_path4run = options.res_path + str(run) + "/" + file_name
        res_file_4run = open(file_path4run, 'r')
        res_lines_4run = res_file_4run.readlines()
                
        meta_files.append(res_file_4run)
        meta_lines_res_file.append(res_lines_4run)
    
    n_len = len(meta_lines_res_file[0])
    acc = 0.0
    for n_idx in range(len(meta_lines_res_file[0])):
        
        prob_insts = 0
        str_line = meta_lines_res_file[0][n_idx];
        temp_res = 'Accuracy:' in str_line
        if temp_res:
            line_split = meta_lines_res_file[0][n_idx].strip().split(' ')
            acc += float(line_split[2])
            for i in range(1, n_runs):
                line_split = meta_lines_res_file[i][n_idx].strip().split(' ')
                acc += float(line_split[2])
                
            acc_avg = acc/n_runs
            #str_temp = str(prob_insts_avg) + " " + str(acc_avg)
            n_len = len(file_name) - len('_test.txt')
            file_name = file_name[:n_len]
            str_temp = "{:s}, {:.4f} \n".format(file_name, acc_avg)
            avg_file.write(str_temp)
        test = 0
            
    #Close all files
    for run in range(n_runs):
        meta_files[run].close()
    
    meta_files.clear()
    meta_lines_res_file.clear()

#avg_file.flush()
avg_file.close()
    



