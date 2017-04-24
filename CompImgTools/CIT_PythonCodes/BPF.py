## Band Pass filters with Sobel kernels.
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
from scipy import ndimage

def make_sqrimg_fft():
    arr = np.random.rand(1024,1024)
    arr = arr>0.99999
    ker = np.zeros_like(arr)
    ker[:30,:30] = 1.
    farr = np.fft.fftn(arr)
    fker = np.fft.fftn(ker)
    return np.abs(np.fft.ifftn(farr*fker))

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
    
img = make_sqrimg_fft()
my_imshow(img)


## Band-Pass filter with right-sobel
ker_right = np.array([[-1, 0, 1],
                      [-2, 0, 2],
                      [-1, 0, 1]])

## Band-Pass filter with left-sobel
ker_left = np.array([[1, 0, -1],
                     [2, 0, -2],
                     [1, 0, -1]])

## Band-Pass filter with top-sobel
ker_top = np.array([[1, 2, 1],
                    [0, 0, 0],
                    [-1, -2, -1]])

## Band-Pass filter with bottom-sobel
ker_bottom = np.array([[-1, -2, -1],
                       [0, 0, 0],
                       [1, 2, 1]])

#my_imshow(ker_right)
#my_imshow(ker_left)
#my_imshow(ker_top)
#my_imshow(ker_bottom)

my_imshow(ndimage.convolve(img, ker_right))
my_imshow(ndimage.convolve(img, ker_left))
my_imshow(ndimage.convolve(img, ker_top))
my_imshow(ndimage.convolve(img, ker_bottom))


#Add noise to the image.
import skimage
from skimage import feature

noisy_img = skimage.util.random_noise(img, mode='s&p', seed=None, clip=True)

my_imshow(noisy_img)

#Apply BPF to the noisy image.
my_imshow((convolution_filter(noisy_img, ker_right)))
