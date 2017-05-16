## Main LBP code.
import skimage
from skimage.feature import local_binary_pattern
from skimage.color import label2rgb
from PIL import Image  
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline


#Creating an Image.
    
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

image = make_img(num_obj=10, obj_rad=12, nr=128, nc=128)

# settings for LBP
radius = 3                # Radius is the spatial resolution of the operator.
n_points = 8 * radius     # Number of circularly symmetric neighbour set points (quantization of the angular space).
METHOD = 'uniform'

def overlay_labels(image, lbp, labels):
    mask = np.logical_or.reduce([lbp == each for each in labels])  # reduce(a, axis=0, dtype=None, out=None, keepdims=False): Reduces `a`'s dimension by one, by applying ufunc along one axis.
    return label2rgb(mask, image=image, bg_label=0, alpha=0.5)     # Return an RGB image where color-coded labels are painted over the image.


lbp = local_binary_pattern(image, n_points, radius, METHOD)   # Return LBP image.


def highlight_bars(bars, indexes):
    for i in indexes:
        bars[i].set_facecolor('r')

def hist(ax, lbp):
    n_bins = int(lbp.max() + 1)
    return ax.hist(lbp.ravel(), normed=True, bins=n_bins, range=(0, n_bins), facecolor='0.5')
                   

# plot histograms of LBP of textures
fig, (ax_img, ax_hist) = plt.subplots(nrows=2, ncols=3, figsize=(9, 6))
plt.gray()

titles = ('edge', 'flat', 'corner')
w = width = radius - 1
edge_labels = range(n_points // 2 - w, n_points // 2 + w + 1)  #range(16//2 -2, 16//2 + 2 + 1) = range(6, 11)
flat_labels = list(range(0, w + 1)) + list(range(n_points - w, n_points + 2)) #list(range(0, 3)) + list(range(14, 18)))
i_14 = n_points // 4            # 1/4th of the histogram # = 4
i_34 = 3 * (n_points // 4)      # 3/4th of the histogram # = 12
corner_labels = (list(range(i_14 - w, i_14 + w + 1)) +   # list(range(2, 7)) + list(range(10, 15))
                 list(range(i_34 - w, i_34 + w + 1)))

label_sets = (edge_labels, flat_labels, corner_labels)

for ax, labels in zip(ax_img, label_sets):
    ax.imshow(overlay_labels(image, lbp, labels))

for ax, labels, name in zip(ax_hist, label_sets, titles):
    counts, _, bars = hist(ax, lbp)
    highlight_bars(bars, labels)
    ax.set_ylim(ymax=np.max(counts[:-1]))
    ax.set_xlim(xmax=n_points + 2)
    ax.set_title(name)

ax_hist[0].set_ylabel('Percentage')
for ax in ax_img:
    ax.axis('off')
    
plt.show()
