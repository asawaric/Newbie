import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
#% matplotlib inline

def make_rectimg_fft():
    arr = np.random.rand(1024,1024)    # Create an array of 1024 lists, each list containing 1024 elements.
    arr = arr>0.9999                   # In the above array, show all the values which are greater than 0.9999.
                                       # This replaces an array 'arr' with elements as 'False' for all the values below 0.9999
                                       # and those above 0.9999 as 'True'.
    ker = np.zeros_like(arr)           # This returns an array of zeros with the same shape and type as a given array.  
    ker[:40,:20] = 1.                  # Make first 10 elements of each list as 'True'. And do this for first 30 lists.
    farr = np.fft.fftn(arr)            # Compute the N-dimensional discrete Fourier Transform.
                                       # This function computes the N-dimensional discrete Fourier Transform over any
                                       # Number of axes in an M-dimensional array by means of the Fast Fourier Transform (FFT).
    fker = np.fft.fftn(ker)            
    return np.abs(np.fft.ifftn(farr*fker))  # Calculate the absolute value element-wise for the inverse FT of resulting array of convolution of farr and fker.

def make_sqrimg_fft():
    arr = np.random.rand(1024,1024)
    arr = arr>0.9999
    ker = np.zeros_like(arr)
    ker[:30,:30] = 1.
    farr = np.fft.fftn(arr)
    fker = np.fft.fftn(ker)
    return np.abs(np.fft.ifftn(farr*fker))

def make_roundimg_fft():
    arr = np.random.rand(1024, 1024)
    arr = arr>0.9999
    ker = np.zeros_like(arr)
    y,x = np.ogrid[-512:511+1, -512:511+1]
    mask = x**2 + y**2 <= 15**2
    ker[mask] = 1
    farr = np.fft.fftn(arr)
    fker = np.fft.fftn(ker)
    return np.abs(np.fft.ifftn(farr*fker))

def make_trilimg_fft():
    arr = np.random.rand(1024,1024)
    arr = arr>0.9999
    ker = np.tri(1024, 1024, 990)
    #ker = np.triu(arr, +1)
    #ker = np.zeros_like(arr)
    #ker = np.tril(ker, +1.)
    farr = np.fft.fftn(arr)
    fker = np.fft.fftn(ker)
    return np.abs(np.fft.ifftn(farr*fker))
  

def my_imshow(arr):
    f,ax = plt.subplots()
    ax.imshow(arr, cmap=cm.gray, interpolation='none')
    plt.show()

img1 = make_rectimg_fft()
my_imshow(img1)

img2 = make_sqrimg_fft()
my_imshow(img2)

img3 = make_roundimg_fft()
my_imshow(img3)

img4 = make_trilimg_fft()
my_imshow(img4)

my_imshow(img4 + img3 + img2 + img1)
