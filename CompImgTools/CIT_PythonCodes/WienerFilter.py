#Applying Wiener filter to blurred (Low pass filtered) image.
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm 
#% matplotlib inline

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

def make_gaussian_kernel(nr=10,nc=10,lpf=2.):
    (X,Y) = 1.*np.mgrid[-1:1:1j*nc,-1:1:1j*nr]
    ker = np.exp(-(X*X+Y*Y)/(lpf*lpf) )
    return ker/ker.max()

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
    
#create an image.
img = make_img(num_obj=4, obj_rad=6, nr=128, nc=128)
my_imshow(img)

#Low pass filter kernel.
ker = make_gaussian_kernel(lpf=1)
my_imshow(ker)

#Convolution of LPF kernel and image.
blurred_img = (convolution_filter(img, ker))
my_imshow(blurred_img)

#Applying wiener filter.
import skimage
from skimage import color, data, restoration
from scipy import signal
WF2 = scipy.signal.wiener(blurred_img, mysize=None, noise=5) 
#my_imshow(WF2)

#Deconvolution for restoration of  convoluted image.
deconvolved_img_out, _ = restoration.unsupervised_wiener(blurred_img, ker)
#deconvolved_img_out, _ = restoration.unsupervised_wiener(WF2, ker)
my_imshow(deconvolved_img_out)
