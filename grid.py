from PIL import Image, ImageOps
import os
from skimage import io, transform, filters, exposure, color
import numpy as np
from numpy import ndarray
import reader
import copy
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

RAWDIR = "all"
OUTDIR = "out"


def make_grid():
    raws, exps = reader.get_images()

    orig = exps['08']
    r = copy.copy(orig)
    g = copy.copy(orig)
    b = copy.copy(orig)


    for i in range(800):
        for j in range(800):
            
            if i % 500 == 0 or j % 500 == 0:
                b[i, j] = 1
            elif i % 100 == 0 or j % 100 == 0:
                r[i, j] = 1
            elif i % 10 == 0 and j % 10 == 0:
                g[i, j] = 1


    #b = np.vectorize(lambda x: min(x, 1.0))(b)

    zipped = np.dstack((r, g, b))
    io.imsave(OUTDIR + '/s_grid.png', zipped)

make_grid()