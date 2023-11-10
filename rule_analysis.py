import numpy as np

feature_path = "../4GECCO-AB-ii/4GECCO-AB-ii/SegSys/MetaData/SegFeatures4Clfrs/"
file_name = "sift_p64b3_hog_d64p32_lbp_r3_dim_64.csv"
train_path = feature_path + "train/" + file_name
test_path = feature_path + "test/" + file_name
ftrs_file = open(train_path,'r')

rules_path = "../4GECCO-AB-ii/4GECCO-AB-ii/SegSys/MetaData/rules.txt"
rules_file = open(rules_path,'r')

n_patch_ftrs = 154

for line in rules_file:
    rule_split = line.strip().split('\t')
    rule_tokens = len(rule_split)    
    n_patch_ftrs = int((rule_tokens - 18)/18)
    print(rule_tokens)
    print(n_patch_ftrs)
    print("Line")
    n_patches = 9
    n_patch_ftrs_sub = n_patch_ftrs*2
    
    for i in range(9, 0, -1):
        print(rule_split[rule_tokens-i])
    
    
    
    for line in ftrs_file:
        ftrs_split = line.strip().split(',')
        n_tokens = len(ftrs_split)
        if n_tokens <500:
            continue
        for i in range(9):
            n_temp = int(rule_split[rule_tokens-9+i])
            if(int(rule_split[rule_tokens-9+i]) != n_patch_ftrs):
                print("SpecificCare")
                b_match = True
                for f in range(0, n_patch_ftrs_sub, 2):
                    n_idx = n_patch_ftrs_sub*i + f
                    n_idx_ftr = int(n_idx/2)
                    print(n_idx)
                    print(n_idx_ftr)
                    print(ftrs_split[n_idx_ftr])
                    print(rule_split[n_idx])
                    print(rule_split[n_idx+1])
                    
                    if(rule_split[n_idx]!= '#'):
                        if(ftrs_split[n_idx_ftr]<rule_split[n_idx]) or (ftrs_split[n_idx_ftr]>rule_split[n_idx+1]):
                            b_match = False
                
            print(rule_split[rule_tokens-9+i])
    
for line in ftrs_file:
    ftrs_split = line.strip().split(',')
    n_tokens = len(ftrs_split)
    if n_tokens >500:
        img_name = ftrs_split[n_tokens-1]
        img_class = ftrs_split[n_tokens-1]
        patch_ftrs = (n_tokens-2)/9
        n_stop = 0
    print(n_tokens)



