# Comaprision of local thresholding with global thresholding.=> Otsu's threshold method applied locally.
# For each pixel, an “optimal” threshold is determined by maximizing the variance between two classes
# of pixels of the local neighborhood defined by a structuring element[1].
## Local thresholding. => In case of a large variation in the background intensity, local/adaptive thresholding 
# may produce a better result[1].
# Code reference from [1] http://scikit-image.org/docs/dev/auto_examples/xx_applications/plot_thresholding.html

import matplotlib.pyplot as plt
from matplotlib import cm
%matplotlib inline
import numpy as np
from PIL import Image

from skimage.filters import threshold_otsu, threshold_local
from skimage.morphology import disk
from skimage.filters import threshold_otsu, rank

def my_imshow(arr):
    f,ax = plt.subplots()
    ax.imshow(arr, cmap=cm.gray, interpolation='none')
    plt.show()

image = np.array(Image.open('Nemo.jpg'))
global_thresh = threshold_otsu(image)
binary_global = image > global_thresh
my_imshow(binary_global)

block_size = 35
adaptive_thresh = threshold_local(image, block_size, offset=10)
binary_adaptive = image > adaptive_thresh
my_imshow(binary_adaptive)
