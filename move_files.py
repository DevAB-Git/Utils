import os
import shutil
import random
from glob import glob

# Path setup.
source = '../MetaData/CatsDog/Imgs/all/dog'
train = '../MetaData/CatsDog/Imgs/train/dog'
test = '../MetaData/CatsDog/Imgs/test/dog'

# Collect files.
files = glob(os.path.join(source, '**'), recursive=True)

# Ensure destination path exists.
if not os.path.isdir(train):
    os.makedirs(train)
if not os.path.isdir(test):
    os.makedirs(test)

n_train=0
n_test=0
# Move all files.
for f in files:
    if os.path.isfile(f):
        base = os.path.basename(f)
        if  random.randint(0, 100) < 80:
            shutil.move(f, os.path.join(train, base))
            n_train+=1;
        else:
            shutil.move(f, os.path.join(test, base))
            n_test+=1

print(n_train)
print(n_test)