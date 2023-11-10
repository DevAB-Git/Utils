import os
import copy
from optparse import OptionParser


parser = OptionParser()

#../NeSI/MetaData/ExpRes/
#parser.add_option("-f", "--res_path", dest="res_path", help="Path to result files", default="../4GECCO-AB-ii/4GECCO-AB-ii/SegSys-iii/MetaData/ExpResSeg/")
parser.add_option("-f", "--res_path", dest="res_path", help="Path to result files", default="../4GECCO-AB-ii/4GECCO-AB-ii/ConvSys-ii/MetaData/ExpRes/")
parser.add_option("-r", "--n_runs", dest="n_runs", help="no of runs", default=5)
parser.add_option("-n", "--common_name", dest="c_name", help="common name for output files", default="_output.txt")

(options, args) = parser.parse_args()

n_runs = options.n_runs
exp_path = options.res_path + "0"

for idxfile, file_name in enumerate(sorted(os.listdir(exp_path))):
    if not file_name.endswith(options.c_name):
        continue
    
    meta_files = []
    meta_lines_res_file = []
    
    file_path = os.path.join(exp_path, file_name)
    file_path_avg = options.res_path + "avg/" + file_name
    
    #res_file = open(file_path, 'r')
    avg_file = open(file_path_avg,'w')
    
    #lines_res_file = res_file.readlines()
    min_probs = 1000;    
    for run in range(n_runs):
        file_path4run = options.res_path + str(run) + "/" + file_name
        res_file_4run = open(file_path4run, 'r')
        res_lines_4run = res_file_4run.readlines()
        
        curr_probs = len(res_lines_4run)
        if curr_probs < min_probs:
            min_probs = curr_probs        
        meta_files.append(res_file_4run)
        meta_lines_res_file.append(res_lines_4run)
    
    n_len = len(meta_lines_res_file[0])
    #for n_idx in range(len(meta_lines_res_file[0])):
    for n_idx in range(min_probs):
        acc = 0.0
        prob_insts = 0
        
        for i in range(n_runs):
            #line = meta_lines_res_file[i][n_idx]
            line_split = meta_lines_res_file[i][n_idx].strip().split(' ')
            prob_insts += int(line_split[0])
            acc += float(line_split[1])
        
        acc_avg = acc/n_runs
        prob_insts_avg = int(prob_insts/n_runs)
        #str_temp = str(prob_insts_avg) + " " + str(acc_avg)
        str_temp = "{:d} {:.4f} \n".format(prob_insts_avg, acc_avg)
        avg_file.write(str_temp)
        test = 0
            
    #Close all files
    avg_file.close()
    for run in range(n_runs):
        meta_files[run].close()
    
    meta_files.clear()
    meta_lines_res_file.clear()





