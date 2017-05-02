## Applying Wiener filter to blurred (Low pass filtered) image. #Figure 'Bridge.jpg'
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm 
#% matplotlib inline

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


from PIL import Image
im = np.array(Image.open('Bridge.jpg'))
my_imshow(im)

data = color.rgb2gray(im)
my_imshow(data)

#Low pass filter kernel.
ker = make_gaussian_kernel(lpf=1)
my_imshow(ker)

#Convolution of LPF kernel and image.
blurred_img = (convolution_filter(data, ker))
my_imshow(blurred_img)


#Applying wiener filter.
import skimage
import scipy
from skimage import color, data, restoration
from scipy import signal
WF2 = scipy.signal.wiener(blurred_img, mysize=None, noise=5) 
#my_imshow(WF2)

#Deconvolution for restoration of convoluted image.
deconvolved_img_out, _ = restoration.unsupervised_wiener(blurred_img, ker)
my_imshow(deconvolved_img_out)
