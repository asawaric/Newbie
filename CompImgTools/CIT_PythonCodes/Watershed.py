from PIL import Image  
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy import ndimage as ndi
%matplotlib inline
import skimage
from skimage import color
from skimage import feature

def my_imshow(arr):
    f,ax = plt.subplots()
    ax.imshow(arr, cmap=cm.gray, interpolation='none')
    plt.show()
    
def make_img(num_obj=100, obj_rad=5, nr=1024, nc=1024):
    arr = np.zeros((nr,nc))
    kerLen = 2*obj_rad
    (X,Y) = np.mgrid[-1:1:1j*kerLen, -1:1:1j*kerLen]
    ker = (np.sqrt(X*X+Y*Y) <= 0.9)
    rand_pos = np.random.rand(num_obj, 2)
    for (x,y) in rand_pos:
        xstart = int(x*(nc-kerLen))
        ystart = int(y*(nr-kerLen))
        arr[xstart:xstart+kerLen, ystart:ystart+kerLen] += ker
    return arr

#Creating an Image.
image = make_img(num_obj=6, obj_rad=10, nr=128, nc=128)
my_imshow(image)

# To separate the circles. We generate markers at the maxima of the distance to the background:
from skimage.feature import peak_local_max
distance = ndi.distance_transform_edt(image)
local_maxi = peak_local_max(distance, labels=image,footprint=np.ones((3, 3)),indices=False)
markers = ndi.label(local_maxi)[0]

#Finally,run the watershed on the image and markers:
from skimage.segmentation import watershed
labels = watershed(-distance, markers, mask=image)
my_imshow(labels)
