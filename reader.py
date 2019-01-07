from PIL import Image, ImageOps
import os
from skimage import io, transform, filters, exposure, color
import numpy as np 
            
RAWDIR = "all"
OUTDIR = "out"

def get_images():
    Image.MAX_IMAGE_PIXELS = None
    raws = {}
    exps = {}
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
            
            raws[adj_fn] = region
            exps[adj_fn] = adhist

    return raws, exps
    

