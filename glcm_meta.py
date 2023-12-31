#########################################################
'''
Statistically, GLCM is a method of examining texture that considers the spatial relationship of pixels.
Within GLCM, we can also derive some statistics that describe more about the texture, such as:
Contrast: Measures the local variations in the gray-level co-occurrence matrix.
Correlation: Measures the joint probability occurrence of the specified pixel pairs.
Energy: Provides the sum of squared elements in the GLCM. Also known as uniformity or the angular second moment.
Homogeneity: Measures the closeness of the distribution of elements in the GLCM to the GLCM diagonal.
'''
#########################################################
import cv2
from google.colab.patches import cv2_imshow

image_spot = cv2.imread(image_file)
gray = cv2.cvtColor(image_spot, cv2.COLOR_BGR2GRAY)

# Find the GLCM
import skimage.feature as feature

# Param:
# source image
# List of pixel pair distance offsets - here 1 in each direction
# List of pixel pair angles in radians
graycom = feature.greycomatrix(gray, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], levels=256)

# Find the GLCM properties
contrast = feature.greycoprops(graycom, 'contrast')
dissimilarity = feature.greycoprops(graycom, 'dissimilarity')
homogeneity = feature.greycoprops(graycom, 'homogeneity')
energy = feature.greycoprops(graycom, 'energy')
correlation = feature.greycoprops(graycom, 'correlation')
ASM = feature.greycoprops(graycom, 'ASM')

print("Contrast: {}".format(contrast))
print("Dissimilarity: {}".format(dissimilarity))
print("Homogeneity: {}".format(homogeneity))
print("Energy: {}".format(energy))
print("Correlation: {}".format(correlation))
print("ASM: {}".format(ASM))