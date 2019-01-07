from PIL import Image, ImageOps
import os
from skimage import io, transform, filters, exposure, color
import numpy as np 
            
RAWDIR = "all"
OUTDIR = "out"

def get_images():
    Image.MAX_IMAGE_PIXELS = None
    images = {}
    for fn in os.listdir(RAWDIR):
        if fn.endswith("TIF"):
            adj_fn = fn.split("_B")[1]
            if len(adj_fn) == 5:
                adj_fn = "0" + adj_fn
            adj_fn = adj_fn[:-4]
            print(adj_fn)

            image = io.imread(RAWDIR + "/" + fn)

            if fn.endswith("8.TIF"):
                pass
                region = image[3500*2:3900*2, 800*2:1200*2]
            else:
                region = image[3500:3900, 800:1200]
                region = transform.resize(region, (800,800), anti_aliasing=False)
            
                #io.imsave("edited/"+adj_fn +".png", region)
            adhist = exposure.equalize_adapthist(region)
            io.imsave(OUTDIR + "/adhist_"+adj_fn +".png", adhist)
            
            images[adj_fn] = adhist

    return images
    



def rgbtest():
    images = get_images()
    print(images.keys())

    # rg = color.gray2rgb(adhist)
    # red_multiplier = [1, 0, 0]
    # yellow_multiplier = [1, 1, 0]
    # rg = red_multiplier * rg
    r = images['04']
    g = images['05']
    b = images['06']
    zipped = np.dstack((r, g, b))
    io.imsave(OUTDIR + "/color.png", zipped)

    # r = images['08']
    # g = images['06']
    # b = images['05']
    b2 = 1-(2*images['05'])
    io.imsave(OUTDIR + "/inv.png", b2)

    io.imsave(OUTDIR + "/color2.png", 
        np.dstack((images['08'], images['05'], images['06'])))
    io.imsave(OUTDIR + "/color3.png", 
        np.dstack((images['04'], images['05'], images['08'])))
    io.imsave(OUTDIR + "/color4.png", 
        np.dstack((images['08'], images['05'], images['04'])))
    io.imsave(OUTDIR + "/color6.png", 
        np.dstack((images['04'], images['08'], b2)))
    io.imsave(OUTDIR + "/true_color.png", 
        np.dstack((images['04'], images['03'], images['02'])))

def sampler():
    images = get_images()
    print(images.keys())


    r = images['08']
    g = images['08']
    b = images['08']

    sample = np.zeros((800,800))
    for i in range(10):
        for j in range(10):
            sample[40+(80*i), 40+(80*j)] = 1
    r = r + sample
    r = np.vectorize(lambda x: min(x, 1.0))(r)

    zipped = np.dstack((r, g, b))
    #zipped = np.dstack((sample, sample, sample))
    io.imsave(OUTDIR + '/sample.png', zipped)

rgbtest()
#sampler()
