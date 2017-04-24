%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

import scipy
from scipy import signal
from scipy import ndimage
from scipy.ndimage import fourier_shift           # Multidimensional Fourier shift filter.

from skimage import data
from skimage.feature import register_translation  #Efficient subpixel image translation registration by cross-correlation. 
from skimage.feature.register_translation import _upsampled_dft 

from PIL import Image

# Define an image.

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
    
##Define or import an image.

image = make_img(num_obj=8, obj_rad=8, nr=512, nc=512)
plt.imshow(image)

## The shift corresponds to the pixel offset relative to the reference image.
shift = (-22.4, 13.32)

## fourier_shift(input, shift) = Multi-dimensional fourier shift filter.
#The array is multiplied with the fourier transform of a shift operation. 
#offset_image is a frequency domain shift of reference image.
offset_image = fourier_shift(np.fft.fftn(image), shift)  # Compute the N-dimensional DFT of an 'image'.
offset_image = np.fft.ifftn(offset_image) #Computes the N-dimensional inverse discrete Fourier Transform.
print("Known offset (y, x): {}".format(shift))

## pixel precision first
shift, error, diffphase = register_translation(image, offset_image)  #Efficient subpixel image 
                                                                     #translation registration by cross-correlation.

fig = plt.figure(figsize=(8, 3))
ax1 = plt.subplot(1, 3, 1, adjustable='box-forced')
ax2 = plt.subplot(1, 3, 2, sharex=ax1, sharey=ax1, adjustable='box-forced')
ax3 = plt.subplot(1, 3, 3)

ax1.imshow(image, cmap='gray')
ax1.set_axis_off()
ax1.set_title('Reference image')

ax2.imshow(offset_image.real, cmap='gray')
ax2.set_axis_off()
ax2.set_title('Offset image')

# Show the output of a cross-correlation to show what the algorithm is
# doing behind the scenes.
image_product = np.fft.fft2(image) *  np.fft.fft2(offset_image).conj()
cc_image = np.fft.fftshift(np.fft.ifft2(image_product))
ax3.imshow(cc_image.real)
ax3.set_axis_off()
ax3.set_title("Cross-correlation")
plt.show()

print("Detected pixel offset (y, x): {}".format(shift))

# subpixel precision
shift, error, diffphase = register_translation(image, offset_image, 100)

fig = plt.figure(figsize=(8, 3))
ax1 = plt.subplot(1, 3, 1, adjustable='box-forced')
ax2 = plt.subplot(1, 3, 2, sharex=ax1, sharey=ax1, adjustable='box-forced')
ax3 = plt.subplot(1, 3, 3)

ax1.imshow(image, cmap='gray')
ax1.set_axis_off()
ax1.set_title('Reference image')

ax2.imshow(offset_image.real, cmap='gray')
ax2.set_axis_off()
ax2.set_title('Offset image')

# Calculate the upsampled DFT, again to show what the algorithm is doing
# behind the scenes.  Constants correspond to calculated values in routine.
cc_image = _upsampled_dft(image_product, 150, 100, (shift*100)+75).conj()
ax3.imshow(cc_image.real)
ax3.set_axis_off()
ax3.set_title("Supersampled XC sub-area")
plt.show()

print("Detected subpixel offset (y, x): {}".format(shift))
