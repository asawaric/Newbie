## To create noisy image and applying HPF on it.

import skimage
from skimage import feature
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
from PIL import Image  
% matplotlib inline

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

def convolution_filter(arr, ker):
    (k_shy, k_shx) = ker.shape    
    padded_ker = np.zeros_like(arr)
    padded_ker[:k_shy, :k_shx] = ker
    farr = np.fft.fftn(arr)
    fker = np.fft.fftn(padded_ker)
    return np.abs(np.fft.ifftn(farr*fker))

def my_imshow(arr):
    f,ax = plt.subplots()
    ax.imshow(arr, cmap=cm.gray, interpolation='none')
    plt.show()

#Creating an Image and kernel.
img = make_img(num_obj=4, obj_rad=10, nr=128, nc=128)
my_imshow(img)

ker = np.array([[-1, -1, -1, -1, -1],
                [-1,  1,  2,  1, -1],
                [-1,  2,  4,  2, -1],
                [-1,  1,  2,  1, -1],
                [-1, -1, -1, -1, -1]])


ker2 = np.array([[-1, -1, -1],
                 [-1,  8, -1],
                 [-1, -1, -1]])


#Add noise to the image.
noisy_img = skimage.util.random_noise(img, mode='s&p', seed=None, clip=True)
my_imshow(noisy_img)

#Apply HPF to the noisy image.
my_imshow((convolution_filter(noisy_img, ker)))
