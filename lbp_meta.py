####################################################################################
#Good link --3rd no
#https://github.com/computervision-xray-testing/pybalu/blob/master/pybalu/feature_extraction/lbp.py
#
####################################################################################
#1St Method
####################################################################################
# import the necessary packages
from skimage import feature
import numpy as np
class LocalBinaryPatterns:
    def __init__(self, numPoints, radius):
        # store the number of points and radius
        self.numPoints = numPoints
        self.radius = radius
    def describe(self, image, eps=1e-7):
        # compute the Local Binary Pattern representation
        # of the image, and then use the LBP representation
        # to build the histogram of patterns
        lbp = feature.local_binary_pattern(image, self.numPoints,
            self.radius, method="uniform")
        (hist, _) = np.histogram(lbp.ravel(),
            bins=np.arange(0, self.numPoints + 3),
            range=(0, self.numPoints + 2))
        # normalize the histogram
        hist = hist.astype("float")
        hist /= (hist.sum() + eps)
        # return the histogram of Local Binary Patterns
        return hist

# import the necessary packages
from pyimagesearch.localbinarypatterns import LocalBinaryPatterns
from sklearn.svm import LinearSVC
from imutils import paths
import argparse
import cv2
import os
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--training", required=True,
    help="path to the training images")
ap.add_argument("-e", "--testing", required=True, 
    help="path to the tesitng images")
args = vars(ap.parse_args())
# initialize the local binary patterns descriptor along with
# the data and label lists
desc = LocalBinaryPatterns(24, 8)
data = []
labels = []
# loop over the training images
for imagePath in paths.list_images(args["training"]):
    # load the image, convert it to grayscale, and describe it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    # extract the label from the image path, then update the
    # label and data lists
    labels.append(imagePath.split(os.path.sep)[-2])
    data.append(hist)
# train a Linear SVM on the data
model = LinearSVC(C=100.0, random_state=42)
model.fit(data, labels)

# loop over the testing images
for imagePath in paths.list_images(args["testing"]):
    # load the image, convert it to grayscale, describe it,
    # and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))
    
    # display the image and the prediction
    cv2.putText(image, prediction[0], (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
        1.0, (0, 0, 255), 3)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    
####################################################################################
#2nd Method
####################################################################################
import cv2
from google.colab.patches import cv2_imshow

class LocalBinaryPatterns:
  def __init__(self, numPoints, radius):
    self.numPoints = numPoints
    self.radius = radius

  def describe(self, image, eps = 1e-7):
    lbp = feature.local_binary_pattern(image, self.numPoints, self.radius, method="uniform")
    (hist, _) = np.histogram(lbp.ravel(), bins=np.arange(0, self.numPoints+3), range=(0, self.numPoints + 2))

    # Normalize the histogram
    hist = hist.astype('float')
    hist /= (hist.sum() + eps)

    return hist, lbp

image = cv2.imread(image_file)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
desc = LocalBinaryPatterns(24, 8)
hist, lbp = desc.describe(gray)
print("Histogram of Local Binary Pattern value: {}".format(hist))

contrast = contrast.flatten()
dissimilarity = dissimilarity.flatten()
homogeneity = homogeneity.flatten()
energy = energy.flatten()
correlation = correlation.flatten()
ASM = ASM.flatten()
hist = hist.flatten()

features = np.concatenate((contrast, dissimilarity, homogeneity, energy, correlation, ASM, hist), axis=0) 
cv2_imshow(gray)
cv2_imshow(lbp)
################################################################
#3rd Methos
################################################################
!pip install import-ipynb
import import_ipynb
from face import face_detection
from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt
from skimage import feature
import numpy as np
import cv2
import os

class LocalBinaryPatterns:
  def __init__(self , numPoints , radius):
    self.numPoints = numPoints
    self.radius = radius

  def describe(self , image , eps=1e-7):
    lbp = feature.local_binary_pattern(image , self.numPoints , self.radius)
    hist = plt.hist(lbp.ravel())
    return lbp , hist

desc = LocalBinaryPatterns(8 , 2)

def preprocess_img(imagePath):
  img = cv2.imread(imagePath)
  rects = face_detection(img)
  for (x , y , w , h) in rects:
    face = img[y:y+h , x:x+w]

  face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
  # plt.imshow(face , cmap="gray")
  # print(face.shape)
  # face = np.array(face)
  
  lbp , hist = desc.describe(face)
  return lbp , hist
  
imagePath = "celeb-data/Tom_Cruise/Tom_Cruise_2.jpg"
     

lbp , hist = preprocess_img(imagePath)
plt.figure(figsize=(8,8))
plt.imshow(lbp , cmap="gray")
# plt.savefig("output/extraction-results/extracted-face.png")
###########################################################
##A good resource
#https://github.com/computervision-xray-testing/pybalu/blob/master/pybalu/feature_extraction/lbp.py
#######################################
__all__ = ['lbp_features', 'LBPExtractor']

import numpy as np
from pybalu.misc import im2col
from skimage.feature import local_binary_pattern as _lbp

from pybalu.base import FeatureExtractor


def lbp_features(image, region=None, *, show=False, labels=False, **kwargs):
    '''\
    lbp_features(image, region=None, *, show=False, labels=False, **kwargs)

    Calculates the Local Binary Patterns over a regular grid of patches. It returns an array
    of uniform lbp82 descriptors for `image`, made by the concatenating histograms of each grid 
    cell in the image. Grid size is `hdiv` * `vdiv`

    Parameters 
    ----------
    image: 2 dimensional ndarray
        It represents a grayscale image or just one dimension of color (eg: green channel)
    region: 2 dimensional ndarray, optional
        If not None, must be of same dimensions an image and of a bool-like type. All the pixels
        not set in this region will be set to 0 on `image` before performing LBP calculations.
    hdiv: positive integer
        Number of horizontal divisions to perform on image.
    vdiv: positive integer
        Number of vertical divisions to perform on image.
    samples: positive integer, optional
        Number of circularly symmetric neighbour set points (quantization of the angular space).
        default value is 8 (all neighbours in 2d)
    norm: bool, optional
        If set to True, the output array is normalized so that the sum of all its features 
        equals 1. Default value is False.
    mapping: string, optional
        Reprsents the kind of LBP performed over each block. Options are:
            - 'default': original local binary pattern which is gray scale but not
               rotation invariant.
            - 'ror': extension of default implementation which is gray scale and
               rotation invariant.
            - 'uniform': improved rotation invariance with uniform patterns and
               finer quantization of the angular space which is gray scale and
               rotation invariant.
            - 'nri_uniform': non rotation-invariant uniform patterns variant
               which is only gray scale invariant.
        default value is 'default'.
    radius: integer, optional
        Radius of circle (spatial resolution of the operator). Default is set depending on number 
        of samples
    ret_centers: bool, optional
        If set to True, an array with the centers of each block over which LBP was performed is 
        returned. Default value is False.
    show: bool, optional
        Wether to print or not messages during execution. Default is False.
    labels: bool, optional
        Wether to return a second array that contains the label of each value. 

    Returns
    -------
    labels: ndarray, optional
        A one dimensional string ndarray that contains the labels to each of the features.
        This array is only returned if `labels` is set to True.
    features: ndarray
        A numeric ndarray that contains (`hdiv`*`vdiv`) * `num_patterns` features extracted from 
        `image`. `num_patterns` depends on `mapping` and `samples` and is usually 10, 59 or 256.
    x_centers: integer ndarray, optional
        A one dimensional array of size `hdiv`*`vdiv` that contains the x center 
        coordinate of the blocks generated on image division. only returned if `ret_centers` is 
        set to True.
    y_centers: integer ndarray, optional
        A one dimensional array of size `hdiv`*`vdiv` that contains the y center 
        coordinate of the blocks generated on image division. only returned if `ret_centers` is 
        set to True.

    Examples
    --------
    ( TODO )
    '''
    vdiv = kwargs.pop('vdiv', None)
    hdiv = kwargs.pop('hdiv', None)
    if vdiv is None or hdiv is None:
        raise ValueError('`vdiv` and `hdiv` must be given to lbp.')

    if region is None:
        region = np.ones_like(image)

    samples = kwargs.pop('samples', 8)
    normalize = kwargs.pop('norm', False)
    integral = kwargs.pop('integral', False)
    max_d = kwargs.pop('max_d', None)
    if integral and max_d is None:
        raise ValueError('`max_d` must be set if `integral` is set to True.')

    weight = kwargs.pop('weight', 0)
    mapping = kwargs.pop('mapping', 'default')

    if mapping == 'ror' or mapping == 'default':
        num_patterns = 2 ** samples
    elif mapping == 'uniform':
        num_patterns = samples + 2
    elif mapping == 'nri_uniform':
        num_patterns = 59
    else:
        raise ValueError(f"Unknown mapping: '{mapping}'")

    radius = kwargs.pop('radius', None)
    if radius is None:
        radius = np.log(samples) / np.log(2) - 1

    ret_centers = kwargs.pop('ret_centers', False)

    if len(kwargs) > 0:
        unknowns = "'" + "', '".join(kwargs.keys()) + "'"
        raise ValueError(f"Unknown options given to lbp: {unknowns}")

    if show:
        print('--- extracting local binary patterns features...')
    label = 'LBP'

    # set pixels not within region to 0
    image = image.copy()
    image[~region.astype(bool)] = 0

    code_img = _lbp(image, P=samples, R=radius, method=mapping)
    n, m = code_img.shape
    N, M = image.shape
    Ilbp = np.zeros_like(image)
    i1 = round((N - n)/2)
    j1 = round((M - m)/2)
    Ilbp[i1:i1+n, j1:j1+m] = code_img

# TODO:
#     if integral:
#         hx = inthist(Ilbp+1, max_d)

    ylen = int(np.ceil(n / vdiv))
    xlen = int(np.ceil(m / hdiv))
    grid_img = im2col(code_img, ylen, xlen) + 1

    if weight > 0:
        label = 'W-' + label
        pass
    else:
        desc = np.vstack([np.histogram(grid_img[:, i], num_patterns)[0]
                          for i in range(grid_img.shape[1])])

    lbp_feats = desc.ravel()
    N, M = desc.shape

    if normalize:
        lbp_feats = lbp_feats / lbp_feats.sum()

    if not labels and not ret_centers:
        return lbp_feats

    if labels:
        lbp_labels = []
        for i in range(N):
            for j in range(M):
                lbp_labels.append(
                    f"{label}({i+1},{j+1:>2d}) [{samples},'{mapping}']")
        ret = np.array(lbp_labels), lbp_feats
    else:
        ret = (lbp_feats,)

    if ret_centers:
        dx = 1 / hdiv
        dy = 1 / vdiv
        x = np.linspace(dx / 2, 1 - dx / 2, hdiv)
        y = np.linspace(dy / 2, 1 - dy / 2, vdiv)
        ret = (ret,) + (x, y)

    return ret


class LBPExtractor(FeatureExtractor):
    def __init__(self, *, hdiv=None, vdiv=None, samples=8, norm=False, mapping="default", radius=None):
        self.hdiv = hdiv
        self.vdiv = vdiv
        self.samples = samples
        self.norm = norm
        self.mapping = mapping
        self.radius = radius

    def transform(self, X):
        params = self.get_params()
        return np.array([lbp_features(x, **params) for x in self._get_iterator(X)])

    def get_labels(self):
        return "LBP"
