import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm 
% matplotlib inline

class img_maker(object):
    def __init__(self):
        self.img = None
        self.ker = None
        
    def make_img(self, num_obj=100, obj_rad=5, nr=1024, nc=1024):
        arr = np.zeros((nr,nc))
        kerLen = 2*obj_rad
        (X,Y) = np.mgrid[-1:1:1j*kerLen, -1:1:1j*kerLen]
        ker = (np.sqrt(X*X+Y*Y) <= 0.9)
        rand_pos = np.random.rand(num_obj, 2)
        for (x,y) in rand_pos:
            xstart = int(x*(nc-kerLen))
            ystart = int(y*(nr-kerLen))
            arr[xstart:xstart+kerLen, ystart:ystart+kerLen] += ker
        self.img = arr.copy()
        
        
    def make_rectimg_fft(self):
        arr = np.random.rand(1024,1024)    
        arr = arr>0.99999                                                        
        ker = np.zeros_like(arr)             
        ker[:50,:20] = 1.                  
        farr = np.fft.fftn(arr)                                                 
        fker = np.fft.fftn(ker)             
        self.img = np.abs(np.fft.ifftn(farr*fker)).copy()

    def make_sqrimg_fft(self):
        arr = np.random.rand(1024,1024)
        arr = arr>0.99999
        ker = np.zeros_like(arr)
        ker[:30,:30] = 1.
        farr = np.fft.fftn(arr)
        fker = np.fft.fftn(ker)
        self.img = np.abs(np.fft.ifftn(farr*fker)).copy()
        
    def make_roundimg_fft(self):
        arr = np.random.rand(1024, 1024)
        arr = arr>0.99999
        ker = np.zeros_like(arr)
        y,x = np.ogrid[-512:511+1, -512:511+1]
        mask = x**2 + y**2 <= 15**2
        ker[mask] = 1
        farr = np.fft.fftn(arr)
        fker = np.fft.fftn(ker)
        self.img = np.abs(np.fft.ifftn(farr*fker)).copy()

    def make_trilimg_fft(self):
        arr = np.random.rand(1024,1024)
        arr = arr>0.99999
        #ker = np.zeros_like(arr)
        ker = np.tri(1024, 1024, 990)  
        farr = np.fft.fftn(arr)
        fker = np.fft.fftn(ker)
        self.img = np.abs(np.fft.ifftn(farr*fker)).copy()

    def imshow_img(self):
        f,ax = plt.subplots()
        ax.imshow(self.img, cmap=cm.gray, interpolation='none')
        plt.show()
        
## Using Class img_maker
my_im1 = img_maker()

my_im1.make_img()
my_im1.imshow_img()

my_im1.make_rectimg_fft()
my_im1.imshow_img()

my_im1.make_sqrimg_fft()
my_im1.imshow_img()

my_im1.make_roundimg_fft()
my_im1.imshow_img()

my_im1.make_trilimg_fft()
my_im1.imshow_img()

