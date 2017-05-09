#Morphological Operators Opening and Closing.
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


#Opening
opened = opening(image, selem)
my_imshow(opened, 'opening')

#Closing
fly = image.copy()
fly[10:30, 200:210] = 0

closed = closing(fly, selem)
my_imshow(closed, 'closing')

