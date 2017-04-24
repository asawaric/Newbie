## High-pass filters.

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
from scipy import ndimage

def make_rectimg_fft():
    arr = np.random.rand(1024,1024)    
    arr = arr>0.9999                  
    ker = np.zeros_like(arr)           
    ker[:40,:20] = 1.                  
    farr = np.fft.fftn(arr)                                                   
    fker = np.fft.fftn(ker)            
    return np.abs(np.fft.ifftn(farr*fker)) 
  
def my_imshow(arr):
    f,ax = plt.subplots()
    ax.imshow(arr, cmap=cm.gray, interpolation='none')
    plt.show()


#High Pass Filter.
img = make_rectimg_fft()
my_imshow(img)

ker = np.array([[-1, -1, -1, -1, -1],
                [-1,  1,  2,  1, -1],
                [-1,  2,  4,  2, -1],
                [-1,  1,  2,  1, -1],
                [-1, -1, -1, -1, -1]])
my_imshow(ker)
my_imshow(ndimage.convolve(img, ker))


## High Pass Filter using different kernel.
from PIL import Image
    
img2 = Image.open('/home/asawari/Desktop/Lab/ComputationalImagingTools/FilterImages/all_PNG/lena.png')
data = np.array(img2, dtype=float)
plt.imshow(data, cmap=cm.gray)

ker2 = np.array([[-1, -1, -1],
                 [-1,  8, -1],
                 [-1, -1, -1]])
my_imshow(ker2)
my_imshow(ndimage.convolve(data, ker2))
