from PIL import Image, ImageOps
import os
from skimage import io, transform, filters, exposure, color
import numpy as np
import reader
import copy
            
RAWDIR = "all"
OUTDIR = "out"



def rgbtest():
    raws, exps = reader.get_images()
    print(exps.keys())

    # rg = color.gray2rgb(adhist)
    # red_multiplier = [1, 0, 0]
    # yellow_multiplier = [1, 1, 0]
    # rg = red_multiplier * rg
    r = exps['04']
    g = exps['05']
    b = exps['06']
    zipped = np.dstack((r, g, b))
    io.imsave(OUTDIR + "/color.png", zipped)

    # r = exps['08']
    # g = exps['06']
    # b = exps['05']
    b2 = 1-(2*exps['05'])
    io.imsave(OUTDIR + "/inv.png", b2)

    io.imsave(OUTDIR + "/color2.png", 
        np.dstack((exps['08'], exps['05'], exps['06'])))
    io.imsave(OUTDIR + "/color3.png", 
        np.dstack((exps['04'], exps['05'], exps['08'])))
    io.imsave(OUTDIR + "/color4.png", 
        np.dstack((exps['08'], exps['05'], exps['04'])))
    io.imsave(OUTDIR + "/color6.png", 
        np.dstack((exps['04'], exps['08'], b2)))
    io.imsave(OUTDIR + "/true_color.png", 
        np.dstack((exps['04'], exps['03'], exps['02'])))
    io.imsave(OUTDIR + "/true_color_raw.png", 
        np.dstack((raws['04'], raws['03'], raws['02'])))

def sampler():
    raws, exps = reader.get_images()
    print(exps.keys())


    r = copy.copy(exps['08'])
    g = copy.copy(exps['08'])
    b = copy.copy(exps['08'])


    sample = np.zeros((800,800))
    for i in range(80):
        for j in range(80):
            
            if i % 10 == 0 or j % 10 == 0:
                r[(10*i), (10*j)] = 1
            else:
                b[(10*i), (10*j)] = 1


    #b = np.vectorize(lambda x: min(x, 1.0))(b)

    zipped = np.dstack((r, g, b))
    io.imsave(OUTDIR + '/grid.png', zipped)

#rgbtest()
sampler()

# creeks = [
#     (130,207),
#     (300,322),
#     (190,324),
#     (,),
#     (,),
#     (,),
#     (,),
# ]

# other = [

# ]
