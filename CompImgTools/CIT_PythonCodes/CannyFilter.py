import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from matplotlib import cm
import skimage
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

#Creating an Image and kernel.
img = make_img(num_obj=4, obj_rad=10, nr=128, nc=128)
my_imshow(img)

#Add noise to the image.
noisy_img = skimage.util.random_noise(img, mode='s&p', seed=None, clip=True)
my_imshow(noisy_img)


# First trial with the Canny filter, with the default smoothing
edges1 = feature.canny(noisy_img)
my_imshow(edges1)

# Increase the smoothing for better results
edges2 = feature.canny(noisy_img, sigma=3)
my_imshow(edges2)


#To fill inner part of the butterfly using the ndi.binary_fill_holes function, which uses
# mathematical morphology to fill the holes.
fill_region = ndi.binary_fill_holes(edges2)
my_imshow(fill_region)
