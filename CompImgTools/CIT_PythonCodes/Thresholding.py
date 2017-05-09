# Code reference from [1] http://scikit-image.org/docs/dev/auto_examples/xx_applications/plot_thresholding.html

##Otsu's thresholding method:
#Otsu’s method calculates an “optimal” threshold (red line in the histogram) by maximizing the 
# variance between two classes of pixels, which are separated by the threshold. 
# Equivalently, this threshold minimizes the intra-class variance[1].

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm 
from skimage import color
% matplotlib inline
from PIL import Image

from skimage.filters import threshold_otsu, threshold_local
from skimage.morphology import disk
from skimage.filters import threshold_otsu, rank

def my_imshow(arr):
    f,ax = plt.subplots()
    ax.imshow(arr, cmap=cm.gray, interpolation='none')
    plt.show()
    
#Import an image.
img = np.array(Image.open('Nemo.jpg'))
my_imshow(img)

#Application of Otsu's method.:
thresh = threshold_otsu(img)
binary = img > thresh
my_imshow(binary)

