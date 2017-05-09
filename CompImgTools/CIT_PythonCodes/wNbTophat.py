#Morphological Operators white-tophat and black-tophat.
import matplotlib.pyplot as plt
from matplotlib import cm
%matplotlib inline
import numpy as np
from PIL import Image

from skimage.morphology import erosion, dilation, opening, closing
from skimage.morphology import black_tophat, white_tophat
from skimage.morphology import disk, diamond, rectangle, square, star

def my_imshow(arr, filter_name):
    f,ax = plt.subplots()
    ax.set_title(filter_name)
    #ax.axis('off')
    ax.set_adjustable('box-forced')
    ax.imshow(arr, cmap=cm.gray, interpolation='none')
    plt.show()
    
#Import an image.
image = np.array(Image.open('Butterfly.jpg'))
my_imshow(image, 'original')

#White tophat
fly = img.copy()
fly[340:350, 200:210] = 255
fly[100:110, 200:210] = 0

w_tophat = white_tophat(fly, selem)
my_imshow(w_tophat, 'white-tophat')

#Black tophat
b_tophat = black_tophat(fly, selem)
my_imshow(b_tophat, 'black-tophat')
