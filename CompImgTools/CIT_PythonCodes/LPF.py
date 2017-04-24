import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
#%matplotlib inline

def make_img_fft():
    arr = np.random.rand(1024,1024)
    arr = arr>0.9999
    ker = np.zeros_like(arr)
    ker[:30,:10] = 1.
    farr = np.fft.fftn(arr)
    fker = np.fft.fftn(ker)
    return np.abs(np.fft.ifftn(farr*fker))

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

def low_pass_filter(arr, lpf=0.4):
    (shy, shx) = arr.shape
    (X,Y) = np.mgrid[-1:1:1j*shx,-1:1:1j*shy]
    farr = np.fft.fftn(arr)
    fker = np.fft.ifftshift(np.exp(-(X*X+Y*Y)/(lpf*lpf) ))
    return np.abs(np.fft.ifftn(farr*fker))

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

img = make_img(num_obj=4, obj_rad=10, nr=128, nc=128)
my_imshow(img)
ker = make_gaussian_kernel(lpf=.8)
my_imshow(ker)
my_imshow(convolution_filter(img, ker))
